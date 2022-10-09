from sqlalchemy.orm import Session

from app.models.roles import PermissionModel, RoleModel
from app.models.users import UserModel


def test_user_model(session: Session):
    """
    Test UserModel.
    """
    user = UserModel(
        username="user-name",
        password="user-password",
        short_name="Adit",
    )
    session.add(user)
    session.commit()

    created_user = session.query(UserModel).one()
    assert created_user.username == "user-name"
    assert created_user.password != "user-password"
    assert created_user.short_name == "Adit"
    assert created_user.verify_password("user-password") == 1


def test_role_permissions_model(session: Session):
    """
    Test RoleModel and PermissionModel.
    """
    manager_role = RoleModel(title="Store Manager")

    can_view_store_reports = PermissionModel(action="reports.store")
    can_manage_store_users = PermissionModel(action="users.manage")
    can_rectify_store_sales = PermissionModel(action="sales.rectify")
    manager_role.permissions.append(can_view_store_reports)
    manager_role.permissions.append(can_manage_store_users)
    manager_role.permissions.append(can_rectify_store_sales)

    session.add(manager_role)
    session.commit()

    created_role: RoleModel = session.query(RoleModel).one()
    assert created_role.title == "Store Manager"
    permissions = [p.action for p in created_role.permissions]
    assert set(permissions) == set(["reports.store", "users.manage", "sales.rectify"])
