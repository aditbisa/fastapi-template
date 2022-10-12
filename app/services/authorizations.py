from functools import lru_cache

from app.configs import get_user_roles_config
from app.schemas.authorizations import UserRole


@lru_cache
def get_user_role(role_id: str) -> UserRole:
    """
    Get UserRole base on role id.
    """

    config = get_user_roles_config()
    try:
        role_dict = [r for r in config["roles"] if r["id"] == role_id][0]
    except IndexError:
        raise ValueError(f'No role found for "{role_id}"')
    user_role = UserRole(**role_dict)
    return user_role
