from sqlalchemy import Column, Integer, VARCHAR, DATE, Identity, TIMESTAMP, BOOLEAN, BIGINT
from sqlalchemy.orm import relationship
from database import Base

# Список курьеров
class Courier(Base):
    __tablename__ = "couriers"

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    user_id = Column(BIGINT, unique=False, nullable=False)
    user_name = Column(VARCHAR(50), unique=False, nullable=False)
    city_from = Column(VARCHAR(25), unique=False, nullable=False)
    city_to = Column(VARCHAR(25), unique=False, nullable=False)
    flight_date = Column(DATE, nullable=False)
    phone = Column(VARCHAR(20), unique=False, nullable=False)
    info = Column(VARCHAR(200), unique=False, nullable=False)
    status = Column(BOOLEAN, nullable=False)


