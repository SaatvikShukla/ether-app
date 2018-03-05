"""empty message

Revision ID: c72e0c51633b
Revises: None
Create Date: 2018-03-05 10:05:47.597775

"""

# revision identifiers, used by Alembic.
revision = 'c72e0c51633b'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'user_pkey')
    )
    op.create_index('ix_user_email', 'user', ['email'], unique=True)
    # ### end Alembic commands ###
