from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Insurance Recommender"
    API_V1_STR: str = "/api/v1"

    RISK_SCORE_RULES: list = [
        "ire.core.risk_score.AgeScore",
        "ire.core.risk_score.IncomeScore",
        "ire.core.risk_score.HouseScore",
        "ire.core.risk_score.DependentsScore",
        "ire.core.risk_score.MaritalStatusScore",
        "ire.core.risk_score.VehicleScore",
    ]

    INELIGIBILITY_RULES: list = [
        "ire.core.ineligibility.BasicCheck",
        "ire.core.ineligibility.AgeCheck",
    ]

    class Config:
        case_sensitive = True


settings = Settings()
