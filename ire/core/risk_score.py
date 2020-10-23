from datetime import datetime
from typing import Dict

from ire.core.interfaces import RiskScoreAdapter
from ire.schemas import Insurance, MaritalStatus, OwnershipStatus, UserProfile


class AgeScore(RiskScoreAdapter):
    """
    If the user is under 30 years old
        - deduct 2 risk points from all lines of insurance
    If she is between 30 and 40 years old
        - deduct 1
    """

    def calculate(
        self, profile: UserProfile, risk: Dict[Insurance, int]
    ) -> Dict[Insurance, int]:
        new_risk = risk.copy()

        if profile.age < 30:
            new_risk = {insurance: risk - 2 for insurance, risk in risk.items()}
        elif 30 <= profile.age <= 40:
            new_risk = {insurance: risk - 1 for insurance, risk in risk.items()}

        return new_risk


class IncomeScore(RiskScoreAdapter):
    """
    If her income is above $200k:
        - deduct 1 risk point from all lines of insurance
    """

    def calculate(
        self, profile: UserProfile, risk: Dict[Insurance, int]
    ) -> Dict[Insurance, int]:
        new_risk = risk.copy()

        if profile.income >= 200_000:
            new_risk = {insurance: risk - 1 for insurance, risk in risk.items()}

        return new_risk


class HouseScore(RiskScoreAdapter):
    """
    If the user's house is mortgaged:
        - add 1 risk point to her home score
        - add 1 risk point to her disability score
    """

    def calculate(
        self, profile: UserProfile, risk: Dict[Insurance, int]
    ) -> Dict[Insurance, int]:
        new_risk = risk.copy()

        if (
            profile.house
            and profile.house.ownership_status == OwnershipStatus.mortgaged
        ):
            new_risk[Insurance.home] += 1
            new_risk[Insurance.disability] += 1

        return new_risk


class DependentsScore(RiskScoreAdapter):
    """
    If the user has dependents:
        - add 1 risk point to both the disability and life scores.
    """

    def calculate(
        self, profile: UserProfile, risk: Dict[Insurance, int]
    ) -> Dict[Insurance, int]:
        new_risk = risk.copy()

        if profile.dependents > 0:
            new_risk[Insurance.disability] += 1
            new_risk[Insurance.life] += 1

        return new_risk


class MaritalStatusScore(RiskScoreAdapter):
    """
    If the user is married:
        - add 1 risk point to the life score
        - remove 1 risk point from disability
    """

    def calculate(
        self, profile: UserProfile, risk: Dict[Insurance, int]
    ) -> Dict[Insurance, int]:
        new_risk = risk.copy()

        if profile.marital_status == MaritalStatus.married:
            new_risk[Insurance.life] += 1
            new_risk[Insurance.disability] -= 1

        return new_risk


class VehicleScore(RiskScoreAdapter):
    """
    If the user's vehicle was produced in the last 5 years:
        - add 1 risk point to that vehicle’s score
    """

    def calculate(
        self, profile: UserProfile, risk: Dict[Insurance, int]
    ) -> Dict[Insurance, int]:
        new_risk = risk.copy()
        fiver_years_ago = datetime.now().year - 5

        if profile.vehicle and profile.vehicle.year >= fiver_years_ago:
            new_risk[Insurance.auto] += 1

        return new_risk
