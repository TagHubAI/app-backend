from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import asyncio

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})

@app.get("/slow_call/{time_lapse}")
async def read_root(request: Request, time_lapse: int):
    import time
    await asyncio.sleep(time_lapse)
    return f"Return after {time_lapse} sec!"

