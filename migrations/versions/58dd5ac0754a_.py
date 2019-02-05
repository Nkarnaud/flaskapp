"""empty message

Revision ID: 58dd5ac0754a
Revises: 0cc726e663ea
Create Date: 2019-02-03 11:31:40.374936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58dd5ac0754a'
down_revision = '0cc726e663ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('status', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'status')
    # ### end Alembic commands ###
