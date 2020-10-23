import pytest
from ire.schemas import Insurance, UserProfile

from ire.core.risk_score import AgeScore


@pytest.fixture
def zero_risk():
    """
    All zero risk dictionary
    """
    return {i: 0 for i in Insurance}


@pytest.mark.parametrize(
    "age,value",
    [
        (20, -2),
        (29, -2),
        (30, -1),
        (40, -1),
        (41, 0),
        (50, 0),
    ],
)
def test_age_score(profile_payload, zero_risk, age, value):
    profile_payload["age"] = age
    profile = UserProfile(**profile_payload)

    risk = AgeScore().calculate(profile, zero_risk)
    assert all(v == value for v in risk.values())


# TODO: finish test for all rules...
