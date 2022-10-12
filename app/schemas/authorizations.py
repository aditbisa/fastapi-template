from typing import List

from app.schemas import BaseSchema


class UserRole(BaseSchema):
    """
    User role schema based on user roles config.
    """

    id: str
    name: str
    description: str
    permissions: List[str]

    def can_do(self, action: str) -> bool:
        """
        Check if user has permission to do action.
        """
        return action in self.permissions
