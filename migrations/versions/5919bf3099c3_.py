"""empty message

Revision ID: 5919bf3099c3
Revises: 35a32aea5b60
Create Date: 2021-11-07 00:33:01.733765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5919bf3099c3'
down_revision = '35a32aea5b60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('review_id', sa.Integer(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['review_id'], ['menu.id'], name=op.f('fk_review_review_id_menu'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_review'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    # ### end Alembic commands ###
