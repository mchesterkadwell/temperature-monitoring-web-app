"""empty message

Revision ID: a0b2d08ee68a
Revises: 
Create Date: 2018-11-26 22:08:01.741199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0b2d08ee68a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('readings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topic', sa.String(length=64), nullable=True),
    sa.Column('therm_id', sa.Integer(), nullable=True),
    sa.Column('channel', sa.Integer(), nullable=True),
    sa.Column('battery', sa.String(length=64), nullable=True),
    sa.Column('brand', sa.String(length=64), nullable=True),
    sa.Column('model', sa.String(length=64), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('temp_c', sa.Numeric(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('readings')
