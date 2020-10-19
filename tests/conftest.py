import pytest


@pytest.fixture
def profile_payload() -> dict:
    """
    Example of user profile payload
    :return: dict with a profile correctly filled
    """
    return {
        "age": 25,
        "dependents": 0,
        "income": 50000,
        "marital_status": "single",
        "risk_questions": [0, 0, 0],
        "house": {"ownership_status": "mortgaged"},
        "vehicle": {"year": 2015},
    }
