from datetime import datetime
from typing import List, Optional, Union

from stac_fastapi.types import stac as stac_types
from stac_fastapi.types.core import AsyncBaseCoreClient, NumType
from stac_fastapi.types.search import Search


class SqlalchemyBackend(AsyncBaseCoreClient):
    async def post_search(
        self, search_request: Search, **kwargs
    ) -> stac_types.ItemCollection:
        pass

    async def get_search(
        self,
        collections: Optional[List[str]] = None,
        ids: Optional[List[str]] = None,
        bbox: Optional[List[NumType]] = None,
        datetime: Optional[Union[str, datetime]] = None,
        limit: Optional[int] = 10,
        query: Optional[str] = None,
        token: Optional[str] = None,
        fields: Optional[List[str]] = None,
        sortby: Optional[str] = None,
        **kwargs,
    ) -> stac_types.ItemCollection:
        pass

    async def get_item(
        self, item_id: str, collection_id: str, **kwargs
    ) -> stac_types.Item:
        pass

    async def all_collections(self, **kwargs) -> stac_types.Collections:
        pass

    async def get_collection(
        self, collection_id: str, **kwargs
    ) -> stac_types.Collection:
        pass

    async def item_collection(
        self, collection_id: str, limit: int = 10, token: Optional[str] = None, **kwargs
    ) -> stac_types.ItemCollection:
        pass
