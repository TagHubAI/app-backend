from typing import Union
from sqlalchemy.orm import Session

from fastapi import FastAPI, Request, Depends 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import asyncio

from . import crud, models, schemas
from ..sql_app.database import SessionLocal, engine

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

@app.get("/slow_call/{time_lapse}")
async def slow_call(request: Request, time_lapse: int):
    import time
    await asyncio.sleep(time_lapse)
    return f"Return after {time_lapse} sec!"

