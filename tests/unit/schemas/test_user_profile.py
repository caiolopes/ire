import pytest
from pydantic import ValidationError

from ire.schemas import UserProfile


def test_general_structure(profile_payload):
    profile = UserProfile(**profile_payload)

    assert profile.dict() == profile_payload


@pytest.mark.parametrize("field", ["age", "dependents", "income"])
def test_negative_values_gives_validation_error(field, profile_payload):
    profile_payload[field] = -1
    with pytest.raises(ValidationError, match="greater than or equal to 0"):
        UserProfile(**profile_payload)


@pytest.mark.parametrize(
    "value, match",
    [
        ([0, 0, 0, 0], "length should be 3"),
        ([], "length should be 3"),
        ([2, 1, 0], "risk answers must be 0 or 1"),
        ([-1, 2, 1], "risk answers must be 0 or 1"),
    ],
)
def test_risk_questions_validation(value, match, profile_payload):
    profile_payload["risk_questions"] = value
    with pytest.raises(ValidationError, match=match):
        UserProfile(**profile_payload)
