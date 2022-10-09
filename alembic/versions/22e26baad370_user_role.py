"""user role

Revision ID: 22e26baad370
Revises: 7bd36b0b3dda
Create Date: 2022-10-09 21:49:21.360714

"""
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import BIGINT

from alembic import op

# revision identifiers, used by Alembic.
revision = "22e26baad370"
down_revision = "7bd36b0b3dda"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("role_id", BIGINT(unsigned=True), sa.ForeignKey("roles.id"), nullable=False),
    )


def downgrade() -> None:
    op.drop_column("users", "role_id")
