"""add readings table

Revision ID: 5492fb5321cb
Revises: 
Create Date: 2018-11-29 22:00:58.764050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5492fb5321cb'
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
