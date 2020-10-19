import abc
from typing import Dict

from app.schemas import Insurance, ScoreEnum, UserProfile


class RiskScore(abc.ABC):
    @abc.abstractmethod
    def calculate(
        self, profile: UserProfile, risk: Dict[Insurance, int]
    ) -> Dict[Insurance, int]:
        raise NotImplementedError


class IneligibilityCheck(abc.ABC):
    @abc.abstractmethod
    def check(
        self, profile: UserProfile, risk: Dict[Insurance, ScoreEnum]
    ) -> Dict[Insurance, ScoreEnum]:
        raise NotImplementedError
