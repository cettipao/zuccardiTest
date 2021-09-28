from fastapi import APIRouter, status, Response, Depends, HTTPException
from bson import ObjectId
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT
from typing import List
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .models import Estacion30300
from config.db import conn
from .schemas import Estacion30300Entity, Estacion30300Entities

estaciones = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@estaciones.get('/estacion30300', response_model=List[Estacion30300], tags=["estacion30300"])
async def find_all_registros(token: str = Depends(oauth2_scheme)):
    return Estacion30300Entities(conn.local.estacion.find())


@estaciones.post('/estacion30300', response_model=Estacion30300, tags=["estacion30300"])
async def create_registro(estacion: Estacion30300, token: str = Depends(oauth2_scheme)):
    new_estacion = dict(estacion)
    del new_estacion["id"]
    id = conn.local.estacion.insert_one(new_estacion).inserted_id
    estacion = conn.local.estacion.find_one({"_id": id})
    return Estacion30300Entity(estacion)


@estaciones.get('/estacion30300/{id}', response_model=Estacion30300, tags=["estacion30300"])
async def find_registro(id: str, token: str = Depends(oauth2_scheme)):
    return Estacion30300Entity(conn.local.estacion.find_one({"_id": ObjectId(id)}))


@estaciones.put("/estacion30300/{id}", response_model=Estacion30300, tags=["estacion30300"])
async def update_registro(id: str, estacion: Estacion30300, token: str = Depends(oauth2_scheme)):
    conn.local.estacion.find_one_and_update({
        "_id": ObjectId(id)
    }, {
        "$set": dict(estacion)
    })
    return Estacion30300Entity(conn.local.estacion.find_one({"_id": ObjectId(id)}))


@estaciones.delete("/estacion30300/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["estacion30300"])
async def delete_registro(id: str, token: str = Depends(oauth2_scheme)):
    conn.local.estacion.find_one_and_delete({
        "_id": ObjectId(id)
    })
    return Response(status_code=HTTP_204_NO_CONTENT)