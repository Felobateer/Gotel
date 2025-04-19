from pydantic import BaseModel
from datetime import datetime

class HotelRequest(BaseModel):
    name: str
    address: str
    city: str
    email: str
    website: str
    description: str
    img: str
    created_at: datetime
    updated_at: datetime
    price: float


class HotelResponse(BaseModel):
    hotel_id: str
    name: str
    address: str
    city: str
    email: str
    website: str
    img: str
    created_at: datetime
    updated_at: datetime
    description: str
    price: float
    rating: float
    