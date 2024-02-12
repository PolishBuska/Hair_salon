from fastapi import FastAPI

from api.routers.main import create_main_router


def app_factory():
    _application = FastAPI(
        title="Beauty_salon",
        version="2"

    )
    main_router = create_main_router(
        prefix="/api/v2",
    )
    _application.include_router(
        main_router
    )
    return _application
