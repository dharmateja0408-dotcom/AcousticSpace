

from app.api.router import router
from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.routes.upload import router as upload_router

router = APIRouter()

router.include_router(
    health_router,
    prefix="/health",
    tags=["Health"]
)

router.include_router(
    upload_router,
    prefix="/upload",
    tags=["Upload"]
)