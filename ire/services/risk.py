from typing import Any, Dict, List

from ire.core.config import settings
from ire.core.interfaces import IneligibilityCheckAdpater, RiskScoreAdapter
from ire.core.utils import get_class
from ire.schemas import Insurance, RiskProfile, ScoreEnum, UserProfile


class RiskService:
    def __init__(self, profile: UserProfile) -> None:
        self.profile = profile
        self.risk_score_rules = self._get_rules(settings.RISK_SCORE_RULES)
        self.ineligibility_rules = self._get_rules(settings.INELIGIBILITY_RULES)

    def apply_rules(self) -> RiskProfile:
        """
        This method will go through all the classes
        """
        risk_score_dict = self._build_risk()

        for rule in self.risk_score_rules:
            if issubclass(rule, RiskScoreAdapter):
                risk_score_dict = rule().calculate(self.profile, risk_score_dict)

        risk = self._mapper(risk_score_dict)

        for rule in self.ineligibility_rules:
            if issubclass(rule, IneligibilityCheckAdpater):
                risk = rule().check(self.profile, risk)

        return RiskProfile(**{k.name: v for k, v in risk.items()})

    @staticmethod
    def _build_risk() -> Dict[Insurance, int]:
        return {i: 0 for i in Insurance}

    @staticmethod
    def _mapper(risk: Dict[Insurance, int]) -> Dict[Insurance, ScoreEnum]:

        new_risk = {}
        for ins in iter(Insurance):
            risk_value = risk[ins]

            if risk_value < 0:
                new_risk[ins] = ScoreEnum.economic
            elif risk_value >= 3:
                new_risk[ins] = ScoreEnum.responsible
            else:
                new_risk[ins] = ScoreEnum.regular

        return new_risk

    @staticmethod
    def _get_rules(config: List[str]) -> List[Any]:
        return [get_class(rule) for rule in config]
