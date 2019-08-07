"""Initial Migration

Revision ID: b67bd101ab38
Revises: 52cb08531feb
Create Date: 2019-08-07 17:50:49.405733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b67bd101ab38'
down_revision = '52cb08531feb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('toppings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.drop_table('Roles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Roles',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Roles_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('type', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Roles_pkey')
    )
    op.drop_table('toppings')
    op.drop_table('roles')
    # ### end Alembic commands ###