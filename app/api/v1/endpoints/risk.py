from typing import Any

from fastapi import APIRouter

from app import schemas

router = APIRouter()


@router.post("/", response_model=schemas.RiskProfile)
def create_risk_profile(profile: schemas.UserProfile) -> Any:
    from app.schemas.risk_profile import Score

    return schemas.RiskProfile(
        auto=Score.regular,
        disability=Score.regular,
        home=Score.regular,
        life=Score.regular,
    )
