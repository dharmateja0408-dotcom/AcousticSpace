



from fastapi import APIRouter

from app.history import get_chart_data

router = APIRouter()


@router.get("/confidence")
async def confidence_chart():
    return get_chart_data()