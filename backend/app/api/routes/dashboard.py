



from fastapi import APIRouter

from app.history import get_dashboard_statistics

router = APIRouter()


@router.get("/")
async def dashboard():

    return get_dashboard_statistics()