from fastapi import APIRouter, status, Response, Depends, HTTPException
from bson import ObjectId
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT
from typing import List
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .models import User
from config.db import conn
from .schemas import userEntity, usersEntity

user = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@user.post("/token", tags=["login"])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = conn.local.user.find_one({"username": form_data.username})
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = userEntity(user_dict)
    hashed_password = sha256_crypt.encrypt(form_data.password)
    if not sha256_crypt.verify(form_data.password, user["password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user["username"], "token_type": "bearer"}


@user.get('/users', response_model=List[User], tags=["users"])
async def find_all_users(token: str = Depends(oauth2_scheme)):
    # print(list(conn.local.user.find()))
    return usersEntity(conn.local.user.find())


@user.post('/users', response_model=User, tags=["users"])
async def create_user(user: User, token: str = Depends(oauth2_scheme)):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    del new_user["id"]
    id = conn.local.user.insert_one(new_user).inserted_id
    user = conn.local.user.find_one({"_id": id})
    return userEntity(user)


@user.get('/users/{id}', response_model=User, tags=["users"])
async def find_user(id: str, token: str = Depends(oauth2_scheme)):
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))


@user.put("/users/{id}", response_model=User, tags=["users"])
async def update_user(id: str, user: User, token: str = Depends(oauth2_scheme)):
    conn.local.user.find_one_and_update({
        "_id": ObjectId(id)
    }, {
        "$set": dict(user)
    })
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))


@user.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
async def delete_user(id: str, token: str = Depends(oauth2_scheme)):
    conn.local.user.find_one_and_delete({
        "_id": ObjectId(id)
    })
    return Response(status_code=HTTP_204_NO_CONTENT)