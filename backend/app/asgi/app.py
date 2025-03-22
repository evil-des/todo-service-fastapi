from fastapi import APIRouter, FastAPI
from api.v1.endpoints import user, task
from core.config import core_settings


def create_app():
    app = FastAPI(
        debug=core_settings.DEBUG,
        openapi_url='/api/openapi.json',
        redoc_url='/api/redoc',
        docs_url="/api/docs",
    )
    base_router = APIRouter(prefix="/api")
    v1_router = APIRouter(prefix="/v1", tags=['v1'])
    v1_router.include_router(user.router)
    v1_router.include_router(task.router)

    base_router.include_router(v1_router)
    app.include_router(base_router)

    return app
