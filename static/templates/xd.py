from fastapi import FastAPI, APIRouter, Request
# importamos los archivos de la carpeta router
from routers import products, users, audio, reproducir
from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse
# Nos permite exponer archivos estaticos como imagenes o en este caso musica
from fastapi.staticfiles import StaticFiles 

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root(request: Request):
    return FileResponse('static/templates/index.html')