from fastapi import APIRouter

from ire.api.v1.endpoints import risk

api_router = APIRouter()

api_router.include_router(risk.router, prefix="/risk", tags=["risk"])
