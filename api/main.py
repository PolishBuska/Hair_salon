import uvicorn
from fastapi import FastAPI

from api.routers.main import create_main_router
from config import get_config


def get_app():
    _application = FastAPI(
        title="Beauty_salon",

    )
    main_router = create_main_router(
        prefix="/api/v2",
    )
    _application.include_router(
        main_router
    )
    return _application


app = get_app()


def run():
    settings = get_config()
    uvicorn.run(
        "api.main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=True
    )

