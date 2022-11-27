from typing import List, Optional

from pydantic import Field, root_validator

from app.schemas import BaseSchema
from app.user_roles import USER_PERMISSIONS, UserAction


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
    role: Optional[str] = None
    permissions: Optional[List[UserAction]] = Field(None, exclude=True, repr=False)

    @root_validator(pre=False, skip_on_failure=True)
    def load_user_role(cls, values):
        if values["role"] and values["role"] in USER_PERMISSIONS:
            values["pemissions"] = USER_PERMISSIONS(values["role"])
        return values
