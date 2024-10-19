"""empty message

Revision ID: 877895302aee
Revises: a4943c8ac570
Create Date: 2024-10-19 14:48:05.061035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '877895302aee'
down_revision = 'a4943c8ac570'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=255), server_default=sa.text("''::character varying"), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
