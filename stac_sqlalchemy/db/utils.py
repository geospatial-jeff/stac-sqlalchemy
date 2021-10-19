import json
import os
from contextlib import asynccontextmanager
from typing import Any, Dict

import attr
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


def geojson_to_orm(geoj: Dict[str, Any]):
    return func.ST_SetSRID(func.ST_GeomFromGeoJSON(json.dumps(geoj)), 4326)


@attr.s
class DatabaseSession:
    connection_string: str = attr.ib()
    echo: bool = True
    pool_pre_ping: bool = True

    @classmethod
    def create_from_env(cls):
        return cls(connection_string=os.environ["CONNECTION_STRING"])

    def __attrs_post_init__(self):
        self.engine = create_async_engine(
            self.connection_string, echo=self.echo, pool_pre_ping=self.pool_pre_ping
        )
        self.sessionmaker = sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession
        )

    @asynccontextmanager
    async def start(self):
        async with self.sessionmaker() as session:
            yield session
