from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import upload
from app.api.routes import history
from app.api.routes import dashboard
from app.api.routes import charts

app = FastAPI(
    title="AcousticSpace",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(
    upload.router,
    prefix="/upload",
    tags=["Upload"]
)

app.include_router(
    history.router,
    prefix="/history",
    tags=["History"]
)

app.include_router(

    dashboard.router,

    prefix="/dashboard",

    tags=["Dashboard"]

)

app.include_router(
    charts.router,
    prefix="/charts",
    tags=["Charts"]
)


