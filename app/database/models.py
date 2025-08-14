from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String, index=True)
    city = Column(String, index=True)
    state = Column(String, index=True)
    country = Column(String, index=True)
    postal_code = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)