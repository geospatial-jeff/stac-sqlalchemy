from typing import Any, Dict

from pystac_client import Client as StacApiClient


def create_single_file_stac(
    collection_id: str, stac_api_client: StacApiClient, **kwargs
) -> Dict[str, Any]:
    """Pull some test data out of a STAC API."""
    collection = stac_api_client.get_collection(collection_id).to_dict()
    collection["links"] = []

    items = []
    item_search = stac_api_client.search(collections=collection_id, **kwargs)
    for item in item_search.get_items():
        item = item.to_dict()
        item["links"] = []
        items.append(item)

    return {"type": "FeatureCollection", "features": items, "collections": [collection]}
