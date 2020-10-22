import pytest


@pytest.fixture
def profile_payload() -> dict:
    """
    Example of user profile payload
    :return: dict with a profile correctly filled
    """
    return {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018},
    }
