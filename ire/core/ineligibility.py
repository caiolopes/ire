from typing import Dict

from ire.core.interfaces import IneligibilityCheck
from ire.schemas import Insurance, ScoreEnum, UserProfile


class BasicCheck(IneligibilityCheck):
    def check(
        self, profile: UserProfile, risk: Dict[Insurance, ScoreEnum]
    ) -> Dict[Insurance, ScoreEnum]:
        """
        If the user doesn’t have income, vehicles or houses,
        she is ineligible for disability, auto, and home insurance, respectively.
        """
        new_risk = risk.copy()
        has_house = profile.house and profile.house.ownership_status == "owned"

        if profile.income == 0 and not profile.vehicle and not has_house:
            for insurance in [Insurance.auto, Insurance.home, Insurance.disability]:
                new_risk[insurance] = ScoreEnum.ineligible

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
