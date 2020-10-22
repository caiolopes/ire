import pytest
from ire.schemas import UserProfile, ScoreEnum, Insurance
from ire.core.ineligibility import BasicCheck, AgeCheck


@pytest.fixture
def risk():
    return {i: ScoreEnum.regular for i in Insurance}


@pytest.mark.parametrize(
    "income,vehicle,house",
    [
        (100000, None, None),
        (0, {"year": 2015}, None),
        (0, None, {"ownership_status": "owned"}),
    ],
)
def test_basic_check(profile_payload, income, vehicle, house, risk):
    profile_payload["income"] = income
    profile_payload["vehicle"] = vehicle
    profile_payload["house"] = house

    profile = UserProfile(**profile_payload)
    new_risk = BasicCheck().check(profile, risk)

    assert new_risk == risk


@pytest.mark.parametrize(
    "income,vehicle,house",
    [
        (0, None, None),
        (0, None, {"ownership_status": "mortgaged"}),
    ],
)
def test_basic_check_ineligibile(profile_payload, income, vehicle, house, risk):
    profile_payload["income"] = income
    profile_payload["vehicle"] = vehicle
    profile_payload["house"] = house
    profile = UserProfile(**profile_payload)

    # change only disability, auto and home to ineligible
    expected = {
        k: ScoreEnum.ineligible if k.name in ["disability", "auto", "home"] else v
        for k, v in risk.items()
    }

    new_risk = BasicCheck().check(profile, risk)

    assert new_risk == expected


@pytest.mark.parametrize("age", [20, 30, 40, 50, 59, 60])
def test_age_check(profile_payload, age, risk):
    profile_payload["age"] = 59
    profile = UserProfile(**profile_payload)
    new_risk = AgeCheck().check(profile, risk)

    assert new_risk == risk


@pytest.mark.parametrize("age", [61, 70, 80, 90])
def test_age_ineligibile(profile_payload, age, risk):
    profile_payload["age"] = age
    profile = UserProfile(**profile_payload)

    # change only disability, auto and home to ineligible
    expected = {
        k: ScoreEnum.ineligible if k.name in ["life", "disability"] else v
        for k, v in risk.items()
    }

    new_risk = AgeCheck().check(profile, risk)

    assert new_risk == expected
