"""first-migration

Revision ID: 03c2ef0ed133
Revises:
Create Date: 2021-10-09 12:33:21.250238

"""
from alembic import op  # type:ignore

# revision identifiers, used by Alembic.
revision = "03c2ef0ed133"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE EXTENSION IF NOT EXISTS postgis")
    op.execute("CREATE SCHEMA stac_data")


def downgrade():
    op.execute("DROP SCHEMA stac_data")
    op.execute("DROP EXTENSION IF EXISTS postgis")
