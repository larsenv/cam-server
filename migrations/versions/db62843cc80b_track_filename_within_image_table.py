"""Track filename within image table

Revision ID: db62843cc80b
Revises: 54638df9d06f
Create Date: 2021-03-02 02:34:33.548197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "db62843cc80b"
down_revision = "54638df9d06f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("images", sa.Column("filename", sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("images", "filename")
    # ### end Alembic commands ###
