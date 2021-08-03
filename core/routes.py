from fastapi import APIRouter

from ov import ov


routes = APIRouter()
routes.include_router(ov.router, prefix="/ovision")
