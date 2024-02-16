import uvicorn

from api.middleware import LoggerMiddleware
from api.responses import Healthy
from api.app_factory import app_factory


from infrastructure.dependency import (master_service_stub,
                                       user_service_stub,
                                       user_service_factory,
                                       login_service_stub,
                                       master_service_factory,
                                       login_service_factory,
                                       get_current_user,
                                       current_user_stub,
                                       keycloak_service_factory)

from config import get_config


app = app_factory()
app.dependency_overrides[master_service_stub] = master_service_factory
app.dependency_overrides[user_service_stub] = keycloak_service_factory
app.dependency_overrides[login_service_stub] = login_service_factory
app.dependency_overrides[current_user_stub] = get_current_user

app.add_middleware(LoggerMiddleware)


@app.get('/health')
async def health(a: str):
    return Healthy(status_code=200, detail=f'{a} Healthy', headers={"HEALTH_CHECK": "OK"})


def run():
    settings = get_config()
    uvicorn.run(
        "api.main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=True
    )

