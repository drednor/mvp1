from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "templates"))


@app.get("/home")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
