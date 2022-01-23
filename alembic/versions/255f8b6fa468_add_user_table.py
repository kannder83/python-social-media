"""add user table

Revision ID: 255f8b6fa468
Revises: f8e345df2eaf
Create Date: 2022-01-21 21:06:04.141675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '255f8b6fa468'
down_revision = 'f8e345df2eaf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
