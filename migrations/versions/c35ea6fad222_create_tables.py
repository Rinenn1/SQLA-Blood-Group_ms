"""create tables

Revision ID: c35ea6fad222
Revises: 4bf293419641
Create Date: 2025-03-13 10:25:21.131561

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c35ea6fad222'
down_revision: Union[str, None] = '4bf293419641'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'donors',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('age', sa.Integer, nullable=False),
        sa.Column('contact_info', sa.String(255), nullable=False),
        sa.Column('blood_type', sa.String(3), nullable=False),
        sa.Column('last_donation_date', sa.Date, nullable=True)
    )

    op.create_table(
        'donations',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('donor_id', sa.Integer, sa.ForeignKey('donors.id')),
        sa.Column('donation_date', sa.Date, nullable=False),
        sa.Column('quantity_ml', sa.Integer, nullable=False),
    )

    op.create_table(
        'blood_stock',
        sa.Column('blood_type', sa.String, primary_key=True),
        sa.Column('quantity_ml', sa.Integer, nullable=False),
        sa.Column('last_updated', sa.Date, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('blood_stock')
    op.drop_table('donations')
    op.drop_table('donors')
