"""Initial Migration

Revision ID: 58ee916c5212
Revises: 80f99b2069ab
Create Date: 2021-08-20 20:58:37.940066

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58ee916c5212'
down_revision = '80f99b2069ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitchs', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitchs', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pitchs', type_='foreignkey')
    op.drop_column('pitchs', 'user_id')
    # ### end Alembic commands ###