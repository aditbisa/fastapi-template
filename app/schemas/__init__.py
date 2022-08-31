from pydantic import BaseModel

from app.utils import snake_to_camel


class BaseSchema(BaseModel):
    """
    Base configuration model whose most of schemas in this API inherit from.
    """

    class Config:
        # Check https://pydantic-docs.helpmanual.io/usage/model_config/ for info.
        orm_mode = True
        alias_generator = snake_to_camel
        allow_population_by_field_name = True
