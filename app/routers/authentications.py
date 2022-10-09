from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.authentications import Token
from app.services.authentications import authenticate_user, create_access_token

router = APIRouter()


@router.post(
    "/token",
    response_model=Token,
    tags=["auth"],
)
def login(
    db: Session = Depends(get_db),
    payload: OAuth2PasswordRequestForm = Depends(),
):
    """
    Login endpoint.
    """
    user = authenticate_user(db, payload.username, payload.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(user)
    return Token(access_token=access_token)
