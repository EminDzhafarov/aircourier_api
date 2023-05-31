import json
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update
from models import Courier
from datetime import datetime

async def get_courier(session: AsyncSession, city_from: str, city_to: str):
    today = datetime.today()
    return (await session.scalars(select(Courier)
                              .where(Courier.city_from == city_from)
                              .where(Courier.city_to == city_to)
                              .where(Courier.flight_date >= today).where(Courier.status == True)
                              .order_by(Courier.flight_date))).all()

async def add_courier(session: AsyncSession, data):
    await session.execute(insert(Courier).values(
        user_id=data.user_id,
        user_name=data.user_name,
        city_from=data.city_from,
        city_to=data.city_to,
        flight_date=data.flight_date,
        phone=data.phone,
        info=data.info,
        status=data.status
    )
    )
    await session.commit()

async def del_courier(session: AsyncSession, data):
    await session.execute(update(Courier).values(status=data.status).where(Courier.id == data.id))
    await session.commit()

async def edit_courier(session: AsyncSession, data):
    stmt = update(Courier).where(Courier.id == data["id"])
    for k, v in data.items():
        if v is not None:
            stmt = stmt.values({k: v})

    await session.execute(stmt)
    await session.commit()
    return data