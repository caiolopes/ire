from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class MaritalStatus(str, Enum):
    single = "single"
    married = "married"


class OwnershipStatus(str, Enum):
    mortgaged = "mortgaged"
    owned = "owned"


class House(BaseModel):
    ownership_status: OwnershipStatus


class Vehicle(BaseModel):
    year: int


class UserProfile(BaseModel):
    age: int
    dependents: int
    income: int
    marital_status: MaritalStatus
    risk_questions: List[int]
    house: Optional[House]
    vehicle: Optional[Vehicle]
