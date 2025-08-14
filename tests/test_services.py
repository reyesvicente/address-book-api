import pytest
from app.database.database import SessionLocal
from app.services.address_service import AddressService
from app.api.schemas import AddressCreate, AddressUpdate

@pytest.fixture
def db_session():
    db = SessionLocal()
    yield db
    db.close()

def test_create_address(db_session):
    service = AddressService()
    address_data = {
        "street": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "country": "USA",
        "postal_code": "62704",
        "latitude": 40.7128,
        "longitude": -74.0060
    }
    address = service.create_address(AddressCreate(**address_data), db_session)
    assert address is not None
    assert address.latitude == address_data["latitude"]
    assert address.longitude == address_data["longitude"]

def test_update_address(db_session):
    service = AddressService()
    address_data = {
        "street": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "country": "USA",
        "postal_code": "62704",
        "latitude": 40.7128,
        "longitude": -74.0060
    }
    address = service.create_address(AddressCreate(**address_data), db_session)
    updated_data = {
        "street": "456 Elm St",
        "city": "Springfield",
        "state": "IL",
        "country": "USA",
        "postal_code": "62704",
        "latitude": 41.0,
        "longitude": -75.0
    }
    updated_address = service.update_address(address.id, AddressUpdate(**updated_data), db_session)
    assert updated_address.street == updated_data["street"]
    assert updated_address.latitude == updated_data["latitude"]

def test_delete_address(db_session):
    service = AddressService()
    address_data = {
        "street": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "country": "USA",
        "postal_code": "62704",
        "latitude": 40.7128,
        "longitude": -74.0060
    }
    address = service.create_address(AddressCreate(**address_data), db_session)
    success = service.delete_address(address.id, db_session)
    assert success is True

def test_get_addresses_within_distance(db_session):
    service = AddressService()
    address_data_1 = {
        "street": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "country": "USA",
        "postal_code": "62704",
        "latitude": 40.7128,
        "longitude": -74.0060
    }
    address_data_2 = {
        "street": "456 Elm St",
        "city": "Springfield",
        "state": "IL",
        "country": "USA",
        "postal_code": "62704",
        "latitude": 40.7138,
        "longitude": -74.0070
    }
    service.create_address(AddressCreate(**address_data_1), db_session)
    service.create_address(AddressCreate(**address_data_2), db_session)
    addresses = service.get_addresses_within_distance(40.7128, -74.0060, 2, db_session)
    assert len(addresses) >= 2