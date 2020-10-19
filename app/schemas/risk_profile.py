import enum

from pydantic import BaseModel


class Insurance(enum.Enum):
    auto = enum.auto()
    disability = enum.auto()
    home = enum.auto()
    life = enum.auto()


class ScoreEnum(str, enum.Enum):
    ineligible = "ineligible"
    economic = "economic"
    regular = "regular"
    responsible = "responsible"


class RiskProfile(BaseModel):
    auto: ScoreEnum
    disability: ScoreEnum
    home: ScoreEnum
    life: ScoreEnum
