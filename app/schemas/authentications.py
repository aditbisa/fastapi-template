from app.schemas import BaseSchema


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
