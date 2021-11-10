"""adding test field

Revision ID: f12b70f3a596
Revises: 69eb477fcc92
Create Date: 2021-11-10 16:53:58.940960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f12b70f3a596'
down_revision = '69eb477fcc92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('test', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipe', 'test')
    # ### end Alembic commands ###
