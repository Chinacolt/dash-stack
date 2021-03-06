"""empty message

Revision ID: 2b52e8261507
Revises: 9f9f6374b616
Create Date: 2016-08-27 17:17:07.016592

"""

# revision identifiers, used by Alembic.
revision = '2b52e8261507'
down_revision = '9f9f6374b616'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('provider_password', sa.String(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'provider_password')
    ### end Alembic commands ###
