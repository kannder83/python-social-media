"""create path table

Revision ID: 17972b70273a
Revises: 
Create Date: 2022-01-21 20:38:08.072447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17972b70273a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))


def downgrade():
    op.drop_table('posts')
