from fastapi import APIRouter


router = APIRouter(

)


@router.get('/schedules')
async def get_schedules():
    ...


@router.get('/schedules/{schedule_id}')
async def get_schedule(schedule_id: int):
    ...
