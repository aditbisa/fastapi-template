from typing import Optional

from pydantic import Field, root_validator

from app.schemas import BaseSchema
from app.schemas.authorizations import UserRole
from app.services.authorizations import get_user_role


class Token(BaseSchema):
    """
    Token endpoint response schema.
    """

    access_token: str
    token_type: str = "bearer"


class UserInfo(BaseSchema):
    """
    User info for "sub" in JWT.
    """

    id: int
    short_name: str
    role_id: Optional[str] = None
    role: Optional[UserRole] = Field(None, exclude=True, repr=False)

    @root_validator(pre=False, skip_on_failure=True)
    def load_user_role(cls, values):
        if values["role_id"]:
            values["role"] = get_user_role(values["role"])
        return values
