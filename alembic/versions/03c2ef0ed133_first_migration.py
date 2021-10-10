"""first-migration

Revision ID: 03c2ef0ed133
Revises:
Create Date: 2021-10-09 12:33:21.250238

"""
import sqlalchemy as sa
from geoalchemy2.types import Geometry
from sqlalchemy.dialects.postgresql import JSONB

from alembic import op  # type:ignore

# revision identifiers, used by Alembic.
revision = "03c2ef0ed133"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE EXTENSION IF NOT EXISTS postgis")
    op.execute("CREATE SCHEMA stac_data")

    op.create_table(
        "collections",
        sa.Column("id", sa.VARCHAR(1024), nullable=False, primary_key=True),
        sa.Column("stac_json", JSONB),
        schema="stac_data",
    )

    op.create_table(
        "items",
        sa.Column("id", sa.VARCHAR(1024), nullable=False, primary_key=True),
        sa.Column("collection_id", sa.VARCHAR(1024), nullable=False, index=True),
        sa.Column("geometry", Geometry("POLYGON", srid=4326, spatial_index=True)),
        sa.Column("datetime", sa.TIMESTAMP, nullable=False, index=True),
        sa.Column("stac_json", JSONB),
        sa.ForeignKeyConstraint(["collection_id"], ["stac_data.collections.id"]),
        schema="stac_data",
    )


def downgrade():
    op.execute("DROP TABLE stac_data.items")
    op.execute("DROP TABLE stac_data.collections")
    op.execute("DROP SCHEMA stac_data")
    op.execute("DROP EXTENSION IF EXISTS postgis")
