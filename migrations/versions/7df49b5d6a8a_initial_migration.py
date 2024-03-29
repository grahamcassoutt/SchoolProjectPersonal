"""Initial migration

Revision ID: 7df49b5d6a8a
Revises: 69633396ae9b
Create Date: 2024-03-20 21:12:06.151936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7df49b5d6a8a'
down_revision = '69633396ae9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todonote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(length=5000), nullable=True),
    sa.Column('date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('to_do_note')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('to_do_note',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('data', sa.VARCHAR(length=5000), nullable=True),
    sa.Column('date', sa.DATETIME(), nullable=True),
    sa.Column('userid', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('todonote')
    # ### end Alembic commands ###
