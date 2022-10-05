import logging
from datetime import datetime, timedelta
from typing import Literal, Union

from jose import JWTError, jwt

from app.configs import get_jwt_settings
from app.models import UserModel

JWT_ALGORITHM = "HS256"

logger = logging.getLogger(__name__)


def authenticate_user(db, username: str, password: str) -> Union[UserModel, Literal[False]]:
    """
    Authenticate user using username and password.

    Returns
    -------
    UserModel if success, False otherwise.
    """
    user: UserModel = db.query(UserModel).filter(UserModel.username == username).one_or_none()
    if not user:
        return False

    verification = user.verify_password(password)
    if not verification:
        return False

    if verification == 2:
        # Password rehashed.
        db.commit()

    return user


def create_access_token(user: UserModel) -> str:
    """
    Create access token for user.
    """
    jwt_settings = get_jwt_settings()
    expire = datetime.utcnow() + timedelta(minutes=jwt_settings.expire_minutes)
    data = {
        "sub": str(user.id),
        "exp": expire,
    }
    encoded_jwt = jwt.encode(data, jwt_settings.secret_key.get_secret_value(), JWT_ALGORITHM)
    return encoded_jwt


def verify_access_token(access_token: str) -> Union[int, Literal[False]]:
    """
    Verify access token.

    Returns
    -------
    User Id if success, False otherwise.
    """
    jwt_settings = get_jwt_settings()
    try:
        payload = jwt.decode(
            access_token, jwt_settings.secret_key.get_secret_value(), JWT_ALGORITHM
        )
        user_id = int(payload.get("sub"))

        if user_id:
            return user_id
        else:
            return False
    except JWTError as err:
        logger.debug(err)

    return False
