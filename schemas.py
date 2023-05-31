from pydantic import BaseModel
from datetime import date

class Courier(BaseModel):
    id: int
    user_id: int
    user_name: str
    city_from: str
    city_to: str
    flight_date: date
    phone: str
    info: str
    status: bool


class CourierAdd(BaseModel):
    user_id: int
    user_name: str
    city_from: str
    city_to: str
    flight_date: date
    phone: str
    info: str
    status: bool

class CourierDel(BaseModel):
    id: int
    status: bool = False