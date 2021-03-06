"""empty message

Revision ID: 4ed2e0a85f28
Revises: 
Create Date: 2020-01-26 21:02:44.247351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ed2e0a85f28'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('customer_name', sa.String(length=64), nullable=True),
    sa.Column('customer_password', sa.String(length=12), nullable=True),
    sa.Column('status', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('customer_id')
    )
    op.create_table('item',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(length=64), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('instock', sa.Boolean(), nullable=True),
    sa.Column('category', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('item_id')
    )
    op.create_table('basket',
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.customer_id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['item.item_id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('basket')
    op.drop_table('item')
    op.drop_table('customer')
    # ### end Alembic commands ###
