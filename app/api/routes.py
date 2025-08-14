from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services.address_service import AddressService
from app.api.schemas import AddressCreate, AddressUpdate, AddressResponse

router = APIRouter()
address_service = AddressService()

@router.post("/addresses/", response_model=AddressResponse)
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    return address_service.create_address(address, db)

@router.get("/addresses/{address_id}", response_model=AddressResponse)
def read_address(address_id: int, db: Session = Depends(get_db)):
    address = address_service.get_address(address_id, db)
    if address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return address

@router.put("/addresses/{address_id}", response_model=AddressResponse)
def update_address(address_id: int, address: AddressUpdate, db: Session = Depends(get_db)):
    updated_address = address_service.update_address(address_id, address, db)
    if updated_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return updated_address

@router.delete("/addresses/{address_id}", response_model=None)
def delete_address(address_id: int, db: Session = Depends(get_db)):
    success = address_service.delete_address(address_id, db)
    if not success:
        raise HTTPException(status_code=404, detail="Address not found")
    return Response(status_code=204)

@router.get("/addresses/", response_model=list[AddressResponse])
def get_addresses_within_distance(lat: float, lon: float, distance: float, db: Session = Depends(get_db)):
    addresses = address_service.get_addresses_within_distance(lat, lon, distance, db)
    return addresses