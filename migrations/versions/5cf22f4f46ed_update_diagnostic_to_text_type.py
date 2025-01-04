"""Update diagnostic to Text type

Revision ID: 5cf22f4f46ed
Revises: ba6be0291133
Create Date: 2025-01-03 23:13:19.792610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cf22f4f46ed'
down_revision = 'ba6be0291133'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('jobcards', schema=None) as batch_op:
        batch_op.alter_column('diagnostic',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.Text(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('jobcards', schema=None) as batch_op:
        batch_op.alter_column('diagnostic',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)

    # ### end Alembic commands ###
