from fastapi import APIRouter, Depends

from app.config import oauth2_scheme

router = APIRouter(prefix="/playgrounds")


@router.get("/")
def get_token(token: str = Depends(oauth2_scheme)):
    return {"token": token}
