from stac_fastapi.api.app import StacApi
from stac_fastapi.extensions.core.transaction import TransactionExtension
from stac_fastapi.types.config import ApiSettings

from stac_sqlalchemy.backend import SqlalchemyBackend
from stac_sqlalchemy.db.utils import DatabaseSession
from stac_sqlalchemy.extensions.transactions import TransactionsBackend

from fastapi import FastAPI

settings = ApiSettings()
app = FastAPI(openapi_url=settings.openapi_url)
db_session = DatabaseSession(
    connection_string="postgresql+asyncpg://username:password@localhost:5432/postgis"
)
stac_api = StacApi(
    settings=settings,
    client=SqlalchemyBackend(),
    app=app,
    extensions=[
        TransactionExtension(
            client=TransactionsBackend(session=db_session), settings=settings
        )
    ],
)


def run():
    """Run app from command line using uvicorn if available."""
    try:
        import uvicorn

        uvicorn.run(
            "stac_sqlalchemy.app:app",
            host=settings.app_host,
            port=settings.app_port,
            log_level="info",
            reload=settings.reload,
        )
    except ImportError:
        raise RuntimeError("Uvicorn must be installed in order to use command")


if __name__ == "__main__":
    run()
