"""add content column to posts table

Revision ID: f8e345df2eaf
Revises: 17972b70273a
Create Date: 2022-01-21 21:03:26.154587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8e345df2eaf'
down_revision = '17972b70273a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
