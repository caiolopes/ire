from typing import Dict

from ire.core.interfaces import IneligibilityCheck
from ire.schemas import Insurance, ScoreEnum, UserProfile


class BasicCheck(IneligibilityCheck):
    def check(
        self, profile: UserProfile, risk: Dict[Insurance, ScoreEnum]
    ) -> Dict[Insurance, ScoreEnum]:
        new_risk = risk.copy()
        if profile.income == 0 and not profile.vehicle and not profile.house:
            for insurance in [Insurance.auto, Insurance.home, Insurance.disability]:
                new_risk[insurance] = ScoreEnum.ineligible

        return new_risk


class AgeCheck(IneligibilityCheck):
    def check(
        self, profile: UserProfile, risk: Dict[Insurance, ScoreEnum]
    ) -> Dict[Insurance, ScoreEnum]:
        new_risk = risk.copy()
        if profile.age >= 60:
            for insurance in [Insurance.life, Insurance.disability]:
                new_risk[insurance] = ScoreEnum.ineligible

        return new_risk
