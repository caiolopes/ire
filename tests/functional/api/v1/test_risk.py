import pytest
from fastapi.testclient import TestClient
from ire.core.config import settings

from ire.main import app


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


@pytest.fixture(scope="module")
def endpoint_url():
    return f"{settings.API_V1_STR}/risk/"


def test_ok(client, profile_payload, endpoint_url):
    response = client.post(
        endpoint_url,
        json=profile_payload,
    )
    print(response.text)
    assert response.status_code == 200


def test_validation_error(client, profile_payload, endpoint_url):
    del profile_payload["age"]

    response = client.post(
        endpoint_url,
        json=profile_payload,
    )
    assert response.status_code == 422
