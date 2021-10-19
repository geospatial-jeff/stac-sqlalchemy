import os

import pytest
from pystac_client import Client as StacApiClient

from stac_sqlalchemy.app import app

from .utils import create_single_file_stac

from starlette.testclient import TestClient

PLANETARY_COMPUTER_URL = os.getenv(
    "PLANETARY_COMPUTER_URL", "https://planetarycomputer.microsoft.com/api/stac/v1"
)


@pytest.fixture(scope="session")
def pc_client() -> StacApiClient:
    return StacApiClient.open(url=PLANETARY_COMPUTER_URL)


@pytest.fixture(scope="session")
def get_test_data(pc_client):
    return create_single_file_stac(
        collection_id="naip",
        bbox=(
            -118.40738296508789,
            34.0137518391494,
            -118.3915901184082,
            34.025205466778296,
        ),
        stac_api_client=pc_client,
    )


@pytest.fixture
def test_app():
    with TestClient(app) as app_client:
        yield app_client
