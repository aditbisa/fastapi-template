"""create users table

Revision ID: df2e9e65b115
Revises: 
Create Date: 2022-10-03 00:02:16.018635

"""
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import BIGINT

from alembic import op

# revision identifiers, used by Alembic.
revision = "df2e9e65b115"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", BIGINT(unsigned=True), autoincrement=True, nullable=False),
        sa.Column("username", sa.String(50), nullable=False, unique=True),
        sa.Column("password", sa.String(255), nullable=False),
        sa.Column("short_name", sa.String(20), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("users")
