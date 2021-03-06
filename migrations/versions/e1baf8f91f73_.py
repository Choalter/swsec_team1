"""empty message

Revision ID: e1baf8f91f73
Revises: 45c911a652a1
Create Date: 2021-11-16 16:41:45.993268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1baf8f91f73'
down_revision = '45c911a652a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_menu')
    with op.batch_alter_table('menu', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), server_default='1', nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_menu_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('access', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('access')

    with op.batch_alter_table('menu', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_menu_user_id_user'), type_='foreignkey')
        batch_op.drop_column('user_id')

    op.create_table('_alembic_tmp_menu',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('ingredients', sa.TEXT(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=200), nullable=False),
    sa.Column('price', sa.VARCHAR(length=320), nullable=False),
    sa.Column('sales', sa.VARCHAR(length=200), nullable=True),
    sa.Column('rate', sa.INTEGER(), nullable=True),
    sa.Column('uploaded_date', sa.DATETIME(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_menu_user_id_user', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='pk_menu'),
    sa.UniqueConstraint('name', name='uq_menu_name')
    )
    # ### end Alembic commands ###
