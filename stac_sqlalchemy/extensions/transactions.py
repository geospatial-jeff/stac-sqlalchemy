import attr
import stac_fastapi.types.stac as stac_types
from sqlalchemy import delete
from sqlalchemy.future import select
from stac_fastapi.extensions.core.transaction import AsyncBaseTransactionsClient

from stac_sqlalchemy.db.model import Collection, Item
from stac_sqlalchemy.db.utils import DatabaseSession, geojson_to_orm


@attr.s
class TransactionsBackend(AsyncBaseTransactionsClient):
    session: DatabaseSession = attr.ib()

    async def create_item(self, item: stac_types.Item, **kwargs) -> stac_types.Item:
        async with self.session.start() as session:
            db_entry = Item(
                id=item["id"],
                collection_id=item["collection"],
                geometry=geojson_to_orm(item["geometry"]),
                datetime=item["datetime"],
                stac_json=item,
            )
            session.add(db_entry)
            await session.commit()
        return item

    async def update_item(self, item: stac_types.Item, **kwargs) -> stac_types.Item:
        pass

    async def delete_item(
        self, item_id: str, collection_id: str, **kwargs
    ) -> stac_types.Item:
        async with self.session.start() as session:
            # Fetch the collection
            stmt = select(Item).where(
                Item.id == item_id, Item.collection_id == collection_id
            )
            result = await session.execute(stmt)
            item = result.first()
            stac_json = item[0].stac_json

            # Delete it
            stmt = delete(Item).where(
                Item.id == item_id, Item.collection_id == collection_id
            )
            await session.execute(stmt)
            await session.commit()

        return stac_json

    async def create_collection(
        self, collection: stac_types.Collection, **kwargs
    ) -> stac_types.Collection:
        async with self.session.start() as session:
            db_entry = Collection(id=collection["id"], stac_json=collection)
            session.add(db_entry)
            await session.commit()
        return collection

    async def update_collection(
        self, collection: stac_types.Collection, **kwargs
    ) -> stac_types.Collection:
        pass

    async def delete_collection(
        self, collection_id: str, **kwargs
    ) -> stac_types.Collection:
        async with self.session.start() as session:
            # Fetch the collection
            stmt = select(Collection).where(Collection.id == collection_id)
            result = await session.execute(stmt)
            collection = result.first()
            stac_json = collection[0].stac_json

            # Delete it
            stmt = delete(Collection).where(Collection.id == collection_id)
            await session.execute(stmt)
            await session.commit()

        return stac_json
