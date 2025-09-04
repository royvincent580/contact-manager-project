"""Create database

Revision ID: 358edf74bd93
Revises: bdcf0956a739
Create Date: 2025-09-03 16:04:34.277378

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '002_create_database'
down_revision: Union[str, Sequence[str], None] = '001_initial_migration'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create database schema."""
    # Database creation handled by SQLite automatically
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
