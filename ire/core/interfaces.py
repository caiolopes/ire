import abc
from typing import Dict

from ire.schemas import Insurance, ScoreEnum, UserProfile


class RiskScoreAdapter(abc.ABC):
    @abc.abstractmethod
    def calculate(
        self, profile: UserProfile, risk: Dict[Insurance, int]
    ) -> Dict[Insurance, int]:
        raise NotImplementedError


class IneligibilityCheckAdpater(abc.ABC):
    @abc.abstractmethod
    def check(
        self, profile: UserProfile, risk: Dict[Insurance, ScoreEnum]
    ) -> Dict[Insurance, ScoreEnum]:
        raise NotImplementedError
