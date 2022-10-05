from app.schemas import BaseSchema


class Token(BaseSchema):
    access_token: str
    token_type: str = "bearer"
