from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, PositiveInt, validator


class MaritalStatus(str, Enum):
    single = "single"
    married = "married"


class OwnershipStatus(str, Enum):
    mortgaged = "mortgaged"
    owned = "owned"


class House(BaseModel):
    ownership_status: OwnershipStatus


class Vehicle(BaseModel):
    year: PositiveInt


class UserProfile(BaseModel):
    age: int = Field(ge=0)
    dependents: int = Field(ge=0)
    income: int = Field(ge=0)
    marital_status: MaritalStatus
    risk_questions: List
    house: Optional[House]
    vehicle: Optional[Vehicle]

    class Config:
        allow_mutation = False

    @validator("risk_questions")
    def questions_must_be_zero_or_one(cls, answers: List) -> List:
        if len(answers) != 3:
            raise ValueError("risk answers length should be 3")
        for ans in answers:
            if ans not in [0, 1]:
                raise ValueError("risk answers must be 0 or 1")
        return answers
