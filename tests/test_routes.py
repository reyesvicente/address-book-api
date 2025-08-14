import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_create_address(client):
    payload = {
        "street": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "country": "USA",
        "postal_code": "62704",
        "latitude": 40.7128,
        "longitude": -74.0060
    }
    response = client.post("/addresses/", json=payload)
    assert response.status_code == 200 or response.status_code == 201
    assert "id" in response.json()
    # Return the created id for use in other tests
    return response.json()["id"]

def test_get_address(client):
    address_id = test_create_address(client)
    response = client.get(f"/addresses/{address_id}/")
    assert response.status_code == 200
    assert response.json()["id"] == address_id

def test_update_address(client):
    address_id = test_create_address(client)
    payload = {
        "street": "456 Elm St",
        "city": "Springfield",
        "state": "IL",
        "country": "USA",
        "postal_code": "62704",
        "latitude": 41.0,
        "longitude": -75.0
    }
    response = client.put(f"/addresses/{address_id}/", json=payload)
    assert response.status_code == 200
    assert response.json()["street"] == "456 Elm St"

def test_delete_address(client):
    address_id = test_create_address(client)
    response = client.delete(f"/addresses/{address_id}/")
    assert response.status_code == 204

def test_get_addresses_within_distance(client):
    response = client.get("/addresses/?lat=40.7128&lon=-74.0060&distance=10")
    assert response.status_code == 200
    assert isinstance(response.json(), list)