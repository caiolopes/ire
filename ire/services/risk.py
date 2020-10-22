from abc import ABC
from types import ModuleType
from typing import Dict, List, Type

from ire.core import risk_score, ineligibility
from ire.core.interfaces import RiskScore, IneligibilityCheck
from ire.schemas import Insurance, ScoreEnum, RiskProfile, UserProfile


class RiskService:
    def __init__(self, profile: UserProfile) -> None:
        self.profile = profile
        self.risk_score_rules = self._get_rules(risk_score, RiskScore)
        self.ineligibility_rules = self._get_rules(ineligibility, IneligibilityCheck)

    def apply_rules(self) -> RiskProfile:
        risk_score_dict = self._build_risk()

        for rule in self.risk_score_rules:
            if issubclass(rule, RiskScore):
                risk_score_dict = rule().calculate(self.profile, risk_score_dict)

        risk = self._mapper(risk_score_dict)

        for rule in self.ineligibility_rules:
            if issubclass(rule, IneligibilityCheck):
                risk = rule().check(self.profile, risk)

        return RiskProfile(**{k.name: v for k, v in risk.items()})

    @staticmethod
    def _build_risk() -> Dict[Insurance, int]:
        return {i: 0 for i in Insurance}

    @staticmethod
    def _get_rules(module: ModuleType, base_class: Type[ABC]) -> List[Type[ABC]]:
        rules = []
        for v in vars(module).values():
            try:
                if issubclass(v, base_class) and v.__name__ != base_class.__name__:
                    rules.append(v)
            except TypeError:
                pass

        return rules

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
