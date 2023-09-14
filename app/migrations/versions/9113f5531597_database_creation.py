"""Database creation

Revision ID: 9113f5531597
Revises:
Create Date: 2023-09-05 18:23:12.579250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9113f5531597"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "fundings",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("symbol", sa.String(), nullable=False),
        sa.Column("rate", sa.Float(), nullable=False),
        sa.Column("date_time", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("admin", sa.Boolean(), nullable=False),
        sa.Column("subscriber", sa.Boolean(), nullable=False),
        sa.Column("pending", sa.Boolean(), nullable=False),
        sa.Column("banned", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    op.drop_table("fundings")
    # ### end Alembic commands ###
