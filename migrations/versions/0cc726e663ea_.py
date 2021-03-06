"""empty message

Revision ID: 0cc726e663ea
Revises: aa69ac3e638e
Create Date: 2019-02-03 11:31:20.977773

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0cc726e663ea'
down_revision = 'aa69ac3e638e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
