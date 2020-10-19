from typing import Any

from fastapi import APIRouter

from app import schemas
from app.services.risk import RiskService

router = APIRouter()


@router.post("/", response_model=schemas.RiskProfile)
def create_risk_profile(profile: schemas.UserProfile) -> Any:
    service = RiskService(profile)
    risk = service.apply_rules()

    return risk
