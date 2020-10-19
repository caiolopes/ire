from enum import Enum

from pydantic import BaseModel


class Score(str, Enum):
    economic = "economic"
    regular = "regular"
    responsible = "responsible"


class RiskProfile(BaseModel):
    auto: Score
    disability: Score
    home: Score
    life: Score
