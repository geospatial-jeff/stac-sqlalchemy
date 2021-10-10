import geoalchemy2 as ga
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()  # type:ignore


class Collection(BaseModel):  # type:ignore

    __tablename__ = "collections"
    __table_args__ = {"schema": "stac_data"}

    id = sa.Column(sa.VARCHAR(1024), nullable=False, primary_key=True)
    stac_json = sa.Column(JSONB)

    children = sa.orm.relationship("Item", lazy="dynamic")


class Item(BaseModel):  # type:ignore

    __tablename__ = "items"
    __table_args__ = {"schema": "stac_data"}

    id = sa.Column(sa.VARCHAR(1024), nullable=False, primary_key=True)
    collection_id = sa.Column(
        sa.VARCHAR(1024), sa.ForeignKey(Collection.id), nullable=False
    )
    geometry = sa.Column(ga.Geometry("POLYGON", srid=4326, spatial_index=True))
    datetime = sa.Column(sa.TIMESTAMP(timezone=True), nullable=False)
    stac_json = sa.Column(JSONB)

    parent_collection = sa.orm.relationship("Collection", back_populates="children")
