from fastapi import APIRouter, Depends

from infrastructure.jwt_handler import AuthProvider

router = APIRouter(

)


@router.get('/schedules')
async def get_schedules(current_user: int = Depends(AuthProvider().get_current_user)):
    ...


@router.get('/schedules/{schedule_id}')
async def get_schedule(schedule_id: int):
    ...
