from sqlalchemy.orm import Session
from app.database.models import Address
from app.api.schemas import AddressCreate, AddressUpdate
from app.utils.distance_calculator import calculate_distance

class AddressService:
    def create_address(self, address: AddressCreate, db: Session):
        db_address = Address(**address.dict())
        db.add(db_address)
        db.commit()
        db.refresh(db_address)
        return db_address

    def get_address(self, address_id: int, db: Session):
        return db.query(Address).filter(Address.id == address_id).first()

    def update_address(self, address_id: int, address: AddressUpdate, db: Session):
        db_address = db.query(Address).filter(Address.id == address_id).first()
        if not db_address:
            return None
        for key, value in address.dict().items():
            setattr(db_address, key, value)
        db.commit()
        db.refresh(db_address)
        return db_address

    def delete_address(self, address_id: int, db: Session):
        db_address = db.query(Address).filter(Address.id == address_id).first()
        if not db_address:
            return False
        db.delete(db_address)
        db.commit()
        return True

    def get_addresses_within_distance(self, lat: float, lon: float, distance: float, db: Session):
        addresses = db.query(Address).all()
        return [
            addr for addr in addresses
            if calculate_distance(lat, lon, addr.latitude, addr.longitude) <= distance
        ]