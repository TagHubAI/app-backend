from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import asyncio

from ..db.config import TORTOISE_ORM_CONFIG
from ..db.models import Users, User_Pydantic, UserIn_Pydantic, UserOut_Pydantic

from tortoise.contrib.fastapi import register_tortoise
import starlette.status as status

from typing import List
from typing import Union

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

register_tortoise(app, **TORTOISE_ORM_CONFIG)

@app.get("/")
def get_root():
    return "Hello World! TagHub is awesome!"

@app.get("/api/v1/users", response_model = List[UserOut_Pydantic])
async def get_users():
    return await UserOut_Pydantic.from_queryset(Users.all())

@app.get("/api/v1/users/{user_id}", response_model = UserOut_Pydantic)
async def get_user(user_id: int):
    return await UserOut_Pydantic.from_queryset_single(Users.get(id=user_id))

@app.post("/api/v1/user", response_model = UserOut_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = await Users.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = User_Pydantic.from_queryset_single(Users.get(username=form_data.get('username'))) 

    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

