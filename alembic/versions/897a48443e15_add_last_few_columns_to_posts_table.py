"""add last few columns to posts table

Revision ID: 897a48443e15
Revises: 86620722407a
Create Date: 2022-01-22 20:13:47.368099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '897a48443e15'
down_revision = '86620722407a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
