import json
import logging
from datetime import datetime, timedelta
from typing import Literal, Union

from jose import JWTError, jwt

from app.configs import get_jwt_settings
from app.models.users import UserModel
from app.schemas.authentications import UserInfo

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
    user_info = UserInfo(id=user.id, short_name=user.short_name, role=user.role)
    data = {
        "sub": user_info.json(),
        "exp": expire,
    }
    encoded_jwt = jwt.encode(data, jwt_settings.secret_key.get_secret_value(), JWT_ALGORITHM)
    return encoded_jwt


def verify_access_token(access_token: str) -> Union[UserInfo, Literal[False]]:
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
        sub_dict = json.loads(payload.get("sub"))
        user_info = UserInfo(**sub_dict)
        return user_info
    except JWTError as err:
        logger.debug(err)

    return False
