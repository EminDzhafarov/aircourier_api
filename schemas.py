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

class CourierEdit(BaseModel):
    id: int
    user_id: int | None
    user_name: str | None
    city_from: str | None
    city_to: str | None
    flight_date: date | None
    phone: str | None
    info: str | None
    status: bool | None