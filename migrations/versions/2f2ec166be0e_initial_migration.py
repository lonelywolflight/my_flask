"""Initial migration.

Revision ID: 2f2ec166be0e
Revises: 
Create Date: 2023-05-17 23:45:00.265681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f2ec166be0e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weather')
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'category', ['category_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('category_id')

    op.create_table('weather',
    sa.Column('city', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('temp_lo', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('temp_hi', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('prcp', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###
