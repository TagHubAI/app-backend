from typing import Union
from sqlalchemy.orm import Session

from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
import asyncio

from ..db import crud, models, schemas
from ..db.database import SessionLocal, engine
import starlette.status as status
from typing import List


models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("index.html", {"request":request})

@app.post("/")
async def post_root(request:Request):
    post_content = await request.form()
    post_content = jsonable_encoder(post_content)
    text_list: List[str] = post_content["textarea"].split("\r\n")
    print(text_list)
    return RedirectResponse(
        '/', 
        status_code=status.HTTP_302_FOUND)

@app.get("/slow_call/{time_lapse}")
async def slow_call(request: Request, time_lapse: int):
    import time
    await asyncio.sleep(time_lapse)
    return f"Return after {time_lapse} sec!"

