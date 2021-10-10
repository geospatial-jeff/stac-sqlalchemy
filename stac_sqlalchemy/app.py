from stac_fastapi.api.app import StacApi
from stac_fastapi.types.config import ApiSettings

from stac_sqlalchemy.backend import SqlalchemyBackend

from fastapi import FastAPI

settings = ApiSettings()
app = FastAPI(openapi_url=settings.openapi_url)
stac_api = StacApi(settings=settings, client=SqlalchemyBackend(), app=app)


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
