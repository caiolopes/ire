from typing import Dict, Optional

import pytest

from ire.core.ineligibility import AgeCheck, BasicCheck
from ire.schemas import Insurance, ScoreEnum, UserProfile

CAR = {"year": 2015}
HOUSE = {"ownership_status": "owned"}


def modify_risk(risk: Dict, ineligible=None) -> Optional[Dict]:
    if not ineligible:
        return risk

    return {
        k: ScoreEnum.ineligible if k.name in ineligible else v for k, v in risk.items()
    }


@pytest.fixture
def all_regular_risk():
    """
    All regular risk dictionary
    """
    return {i: ScoreEnum.regular for i in Insurance}


@pytest.mark.parametrize(
    "income,vehicle,house,ineligible",
    [
        # ineligible for all insurances
        (0, None, None, ["disability", "auto", "home"]),
        # eligible for all insurances
        (50000, CAR, HOUSE, []),
        # one cases
        (50000, None, None, ["auto", "home"]),
        (0, CAR, None, ["disability", "home"]),
        (0, None, HOUSE, ["disability", "auto"]),
    ],
)
def test_basic_check(
    profile_payload, income, vehicle, house, all_regular_risk, ineligible
):
    profile_payload["income"] = income
    profile_payload["vehicle"] = vehicle
    profile_payload["house"] = house
    profile = UserProfile(**profile_payload)

    expected_risk = modify_risk(all_regular_risk, ineligible=ineligible)

    risk = BasicCheck().check(profile, all_regular_risk)

    assert risk == expected_risk


@pytest.mark.parametrize("age", [20, 30, 40, 50, 59, 60])
def test_age_check(profile_payload, age, all_regular_risk):
    profile_payload["age"] = 59
    profile = UserProfile(**profile_payload)
    risk = AgeCheck().check(profile, all_regular_risk)

    assert risk == all_regular_risk


@pytest.mark.parametrize("age", [61, 70, 80, 90])
def test_age_ineligibile(profile_payload, age, all_regular_risk):
    profile_payload["age"] = age
    profile = UserProfile(**profile_payload)

    expected_risk = modify_risk(all_regular_risk, ineligible=["life", "disability"])

    risk = AgeCheck().check(profile, all_regular_risk)

    assert risk == expected_risk
