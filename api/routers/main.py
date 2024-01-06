from fastapi import APIRouter

from api.routers.customer import router as customer_r
from api.routers.master import router as master_r
from api.routers.user import router as user_r
from api.routers.login import router as login_r


def create_main_router(prefix):
    _r = APIRouter(
        prefix=prefix,
    )
    _r.include_router(
        login_r,
        tags=['authentication']
    )
    _r.include_router(
        customer_r,
        prefix='/customer',
        tags=['customer']
    )
    _r.include_router(user_r,
                      tags=['registration'])

    _r.include_router(
        master_r,
        prefix='/master',
        tags=['master']
    )
    return _r


