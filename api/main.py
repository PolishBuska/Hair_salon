import uvicorn
from fastapi import FastAPI, Depends

from api.middleware import LoggerMiddleware
from api.routers.main import create_main_router
from api.responses import Healthy

from infrastructure.dependency import master_service_stub, user_service_stub, user_service_factory
from infrastructure.dependency import master_service_factory

from config import get_config


def get_app():
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


app = get_app()
app.dependency_overrides[master_service_stub] = master_service_factory
app.dependency_overrides[user_service_stub] = user_service_factory

app.add_middleware(LoggerMiddleware)


@app.get('/health')
async def health(a: str):
    return Healthy(status_code=200, detail=f'{a} Healthy')


def run():
    settings = get_config()
    uvicorn.run(
        "api.main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=True
    )

