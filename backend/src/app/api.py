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

<<<<<<< HEAD
from ..edakit import visualization
=======
>>>>>>> 4dd4568e45f9ba4e9886fa7377c2114cb5ab52b1

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
    all_data_query = [(i,data.text_content) for i,data in enumerate(db.query(models.Text).all())]
    return templates.TemplateResponse("index.html", {"request":request, "idx_text_list":all_data_query})

@app.post("/")
async def post_root(request:Request, db: Session = Depends(get_db)):
    post_content = await request.form()
    post_content = jsonable_encoder(post_content)
    text_list: List[str] = post_content["textarea"].split("\r\n")

    for txt in text_list:
        crud.create_text(db, schemas.TextBase(text_content=txt))

    return RedirectResponse(
        '/', 
        status_code=status.HTTP_302_FOUND)

@app.get("/slow_call/{time_lapse}")
async def slow_call(request: Request, time_lapse: int):
    import time
    await asyncio.sleep(time_lapse)
    return f"Return after {time_lapse} sec!"

<<<<<<< HEAD
@app.get("/visualization/word_cloud", response_class=HTMLResponse)
def get_word_cloud_visualization(db: Session = Depends(get_db)):
    import numpy as np
    import plotly
    import plotly.express as px

    text_list = [data.text_content for data in db.query(models.Text).all()]
    wc_img: np.array =  visualization.get_wordcloud_visualization(text_list)
    fig = px.imshow(wc_img)
    wc_html = plotly.io.to_html(fig)
    return wc_html
=======
>>>>>>> 4dd4568e45f9ba4e9886fa7377c2114cb5ab52b1
