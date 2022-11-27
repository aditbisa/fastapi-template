from enum import Enum
from typing import Dict, List


class UserRole(str, Enum):
    SysAdmin = "sys-admin"
    Admin = "admin"
    Manager = "manager"


class UserAction(str, Enum):
    ManageAllUsers = "manage-all-users"
    ManageStoreUsers = "manage-store-users"


USER_PERMISSIONS: Dict[UserRole, List[UserAction]] = {
    UserRole.SysAdmin: [
        UserAction.ManageAllUsers,
    ],
    UserRole.Admin: [
        UserAction.ManageAllUsers,
    ],
    UserRole.Manager: [
        UserAction.ManageStoreUsers,
    ],
}
