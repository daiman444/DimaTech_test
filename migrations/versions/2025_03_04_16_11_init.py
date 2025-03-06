"""init

Revision ID: 9e7f7b272427
Revises: 
Create Date: 2025-03-04 16:11:41.390700

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e7f7b272427'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('last_name', sa.String(length=32), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('invoices',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('balance', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payments',
    sa.Column('invoice_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['invoice_id'], ['invoices.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payments')
    op.drop_table('invoices')
    op.drop_table('users')
    # ### end Alembic commands ###
