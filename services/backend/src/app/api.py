from typing import Union

from fastapi import FastAPI, Request, Depends, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
import asyncio

from ..db.register import register_tortoise
from ..db.config import TORTOISE_ORM

import starlette.status as status
from typing import List

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)


@app.get("/")
def get_root():
    return "Hello World!"


@app.post("/")
async def post_root(request: Request):  # , db: Session = Depends(get_db)):
    post_content = await request.form()
    post_content = jsonable_encoder(post_content)
    text_list: List[str] = post_content["textarea"].split("\r\n")

    for txt in text_list:
        crud.create_text(db, schemas.TextBase(text_content=txt))

    return RedirectResponse("/", status_code=status.HTTP_302_FOUND)


@app.get("/slow_call/{time_lapse}")
async def slow_call(request: Request, time_lapse: int):
    import time

    await asyncio.sleep(time_lapse)
    return f"Return after {time_lapse} sec!"
