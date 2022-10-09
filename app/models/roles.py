import logging

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.database import Base

logger = logging.getLogger(__name__)


role_permissions_table = sa.Table(
    "role_permissions",
    Base.metadata,
    sa.Column("role_id", sa.ForeignKey("roles.id"), primary_key=True),
    sa.Column("permission_id", sa.ForeignKey("permissions.id"), primary_key=True),
)


class RoleModel(Base):
    __tablename__ = "roles"

    id = sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True)
    title = sa.Column("title", sa.String(255), nullable=False, unique=True)
    description = sa.Column("description", sa.String(1024), nullable=True)

    permissions = relationship(
        "PermissionModel", secondary=role_permissions_table, back_populates="roles"
    )  # type: ignore


class PermissionModel(Base):
    __tablename__ = "permissions"

    id = sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True)
    action = sa.Column("action", sa.String(255), nullable=False, unique=True)
    description = sa.Column("description", sa.String(1024), nullable=True)

    roles = relationship(
        "RoleModel", secondary=role_permissions_table, back_populates="permissions"
    )  # type: ignore
