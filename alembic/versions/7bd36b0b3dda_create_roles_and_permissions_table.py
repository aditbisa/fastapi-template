"""create roles and permissions table

Revision ID: 7bd36b0b3dda
Revises: df2e9e65b115
Create Date: 2022-10-09 19:10:36.680119

"""
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import BIGINT

from alembic import op

# revision identifiers, used by Alembic.
revision = "7bd36b0b3dda"
down_revision = "df2e9e65b115"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "roles",
        sa.Column("id", BIGINT(unsigned=True), autoincrement=True, nullable=False),
        sa.Column("title", sa.String(255), nullable=False, unique=True),
        sa.Column("description", sa.String(1024), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "permissions",
        sa.Column("id", BIGINT(unsigned=True), autoincrement=True, nullable=False),
        sa.Column("action", sa.String(255), nullable=False, unique=True),
        sa.Column("description", sa.String(1024), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "role_permissions",
        sa.Column("id", BIGINT(unsigned=True), autoincrement=True, nullable=False),
        sa.Column("role_id", BIGINT(unsigned=True), sa.ForeignKey("roles.id"), nullable=False),
        sa.Column(
            "permission_id", BIGINT(unsigned=True), sa.ForeignKey("permissions.id"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("role_permissions")
    op.drop_table("permissions")
    op.drop_table("roles")
