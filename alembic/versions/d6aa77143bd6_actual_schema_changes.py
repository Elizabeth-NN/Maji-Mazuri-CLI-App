"""actual schema changes

Revision ID: d6aa77143bd6
Revises: ba68ec505a70
Create Date: 2025-06-03 15:54:28.121264

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd6aa77143bd6'
down_revision: Union[str, None] = 'ba68ec505a70'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
