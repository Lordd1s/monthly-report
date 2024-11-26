"""initial migration

Revision ID: 613f9d11e79b
Revises: 
Create Date: 2024-11-26 15:50:32.492725

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '613f9d11e79b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('materials',
    sa.Column('title', sa.String(length=32), nullable=False),
    sa.Column('model_name', sa.String(length=50), nullable=False),
    sa.Column('count_type', sa.Enum('KILOGRAM', 'METER', 'PIECE', 'BOBINE', name='counttype'), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('color', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('last_updated_at', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('materials')
    # ### end Alembic commands ###
