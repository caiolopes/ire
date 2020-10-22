from datetime import datetime
from typing import Dict

from ire.core.interfaces import RiskScore
from ire.schemas import UserProfile, OwnershipStatus, MaritalStatus, Insurance


class AgeScore(RiskScore):
    def calculate(
        self, profile: UserProfile, risk: Dict[Insurance, int]
    ) -> Dict[Insurance, int]:
        if profile.age < 30:
            new_risk = {insurance: risk - 2 for insurance, risk in risk.items()}
        elif 30 <= profile.age <= 40:
            new_risk = {insurance: risk - 1 for insurance, risk in risk.items()}
        else:
            new_risk = risk.copy()

        return new_risk


class IncomeScore(RiskScore):
    enabled = True

    def calculate(
        self, profile: UserProfile, risk: Dict[Insurance, int]
    ) -> Dict[Insurance, int]:
        new_risk = risk.copy()

        if profile.income >= 200000:
            new_risk = {insurance: risk - 1 for insurance, risk in risk.items()}

        return new_risk


class HouseScore(RiskScore):
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


class DependentsScore(RiskScore):
    def calculate(
        self, profile: UserProfile, risk: Dict[Insurance, int]
    ) -> Dict[Insurance, int]:
        new_risk = risk.copy()

        if profile.dependents > 0:
            new_risk[Insurance.disability] += 1
            new_risk[Insurance.life] += 1

        return new_risk


class MaritalStatusScore(RiskScore):
    def calculate(
        self, profile: UserProfile, risk: Dict[Insurance, int]
    ) -> Dict[Insurance, int]:
        new_risk = risk.copy()

        if profile.marital_status == MaritalStatus.married:
            new_risk[Insurance.disability] -= 1
            new_risk[Insurance.life] += 1

        return new_risk


class VehicleScore(RiskScore):
    def calculate(
        self, profile: UserProfile, risk: Dict[Insurance, int]
    ) -> Dict[Insurance, int]:
        new_risk = risk.copy()
        fiver_years_ago = datetime.now().year - 5

        if profile.vehicle and profile.vehicle.year >= fiver_years_ago:
            new_risk[Insurance.auto] += 1

        return new_risk
