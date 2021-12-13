"""empty message

Revision ID: 35a32aea5b60
Revises: 0c077a7632f9
Create Date: 2021-11-07 00:21:31.021617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35a32aea5b60'
down_revision = '0c077a7632f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('email', name=op.f('uq_user_email')),
    sa.UniqueConstraint('username', name=op.f('uq_user_username'))
    )
    with op.batch_alter_table('menu', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_menu_name'), ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('menu', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_menu_name'), type_='unique')

    op.drop_table('user')
    # ### end Alembic commands ###