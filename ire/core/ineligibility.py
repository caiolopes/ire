from typing import Dict

from ire.core.interfaces import IneligibilityCheck
from ire.schemas import Insurance, ScoreEnum, UserProfile


class BasicCheck(IneligibilityCheck):
    """
    If the user doesn’t have income, vehicles or houses,
    she is ineligible for disability, auto, and home insurance, respectively.
    """

    def check(
        self, profile: UserProfile, risk: Dict[Insurance, ScoreEnum]
    ) -> Dict[Insurance, ScoreEnum]:

        new_risk = risk.copy()

        if profile.income == 0:
            new_risk[Insurance.disability] = ScoreEnum.ineligible

        if not profile.vehicle:
            new_risk[Insurance.auto] = ScoreEnum.ineligible

        if not profile.house:
            new_risk[Insurance.home] = ScoreEnum.ineligible

        return new_risk


class AgeCheck(IneligibilityCheck):
    """
    If the user is over 60 years old, she is ineligible
    for disability and life insurance.
    """

    def check(
        self, profile: UserProfile, risk: Dict[Insurance, ScoreEnum]
    ) -> Dict[Insurance, ScoreEnum]:
        new_risk = risk.copy()
        if profile.age > 60:
            for insurance in [Insurance.life, Insurance.disability]:
                new_risk[insurance] = ScoreEnum.ineligible

        return new_risk
