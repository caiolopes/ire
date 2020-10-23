from fastapi import FastAPI

from ire.api.v1.routes import api_router
from ire.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix=settings.API_V1_STR)
