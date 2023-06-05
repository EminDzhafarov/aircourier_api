from backend.db import crud
from typing import Any
from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from backend.db.database import get_session
from backend.db.schemas import CourierAdd, CourierDel, CourierEdit, CourierFind
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="AirCourier",
              description="Бот для поиска курьеров",
              version="2.0")

origins = [
    "http://localhost:8000",
    "localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}


@app.get("/api/v1/couriers/")
async def find_couriers(courier: CourierFind, session: AsyncSession = Depends(get_session)) -> Any:
    """
    Получает города: откуда и куда. Возвращает карточку курьера.

    :param courier:
    :param session:
    :return:
    """
    couriers = await crud.get_courier(session, courier)
    if couriers:
        return couriers
    else:
        return JSONResponse(
            content={"message": "Курьеры не найдены"},
            status_code=204
        )


@app.post("/api/v1/couriers/")
async def add_courier(courier: CourierAdd, session: AsyncSession = Depends(get_session)) -> Any:
    """
    Добавляет курьера в базу данных

    :param courier:
    :param session:
    :return:
    """
    await crud.add_courier(session, CourierAdd(**courier.dict()))
    return JSONResponse(content={"message": "Курьер добавлен"},
                        status_code=201)


@app.put("/api/v1/couriers/")
async def edit_courier(courier: CourierEdit, session: AsyncSession = Depends(get_session)) -> Any:
    """
    Редактирует карточку курьера в базе данных

    :param courier:
    :param session:
    :return:
    """
    await crud.edit_courier(session, courier.dict())
    return JSONResponse(content={"message": "Курьер отредактирован"},
                        status_code=201)


@app.delete("/api/v1/couriers/")
async def delete_courier(courier: CourierDel, session: AsyncSession = Depends(get_session)) -> Any:
    """
    Удаляет курьера из базы данных

    :param courier:
    :param session:
    :return:
    """
    await crud.del_courier(session, CourierDel(**courier.dict()))
    return JSONResponse(content={"message": "Курьер удален"},
                        status_code=410)
