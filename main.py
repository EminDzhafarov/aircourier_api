import crud
from typing import Any
from fastapi import Depends, FastAPI, HTTPException, Body
from fastapi.responses import JSONResponse, FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from schemas import Courier, CourierAdd, CourierDel, CourierEdit


app = FastAPI(title="AirCourier",
    description="Бот для поиска курьеров",
    version="2.0")


@app.get("/api/couriers/find")
async def find_couriers(city_from: str, city_to: str, session: AsyncSession = Depends(get_session)) -> Any:
    """
    Получает города: откуда и куда. Возвращает карточку курьера.

    <code>/api/couriers/find</code>

    :param city_from:
    :param city_to:
    :param session:
    :return:
    """
    couriers = await crud.get_courier(session, city_from=city_from, city_to=city_to)
    if couriers:
        return couriers
    else:
        return JSONResponse(
            content={"message": "Курьеры не найдены"},
            status_code=404
        )

@app.post("/api/couriers/add")
async def add_courier(courier: CourierAdd, session: AsyncSession = Depends(get_session)) -> Any:
    """
    Добавляет курьера в базу данных

    <code>/api/couriers/add</code>

    :param courier:
    :param session:
    :return:
    """
    data = CourierAdd(**courier.dict())
    await crud.add_courier(session, data)
    return data, JSONResponse(content={"message": "Курьер добавлен"})

@app.post("/api/couriers/del")
async def delete_courier(courier: CourierDel, session: AsyncSession = Depends(get_session)) -> Any:
    """
    Удаляет курьера из базы данных

    <code>/api/couriers/del</code>

    :param courier:
    :param session:
    :return:
    """
    data = CourierDel(**courier.dict())
    await crud.del_courier(session, data)
    return data, JSONResponse(content={"message": "Курьер удален"})

@app.post("/api/couriers/edit")
async def edit_courier(courier: CourierEdit, session: AsyncSession = Depends(get_session)) -> Any:
    """
    Редактирует карточку курьера в базе данных

    <code>/api/couriers/edit</code>

    :param courier:
    :param session:
    :return:
    """
    data = await crud.edit_courier(session, courier.dict())
    return data, JSONResponse(content={"message": "Курьер отредактирован"})