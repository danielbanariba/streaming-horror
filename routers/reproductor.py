import av
from fastapi import FastAPI, Request, Header, Stream
from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse, Response
from fastapi.staticfiles import StaticFiles
from os import getcwd, path

router = FastAPI()

router.mount("/static", StaticFiles(directory="static"), name="static")

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return FileResponse('static/templates/index.html')

# Ruta para servir archivos de películas
@router.get("/movies/{movie_name}")
async def read_movie(movie_name: str):
    file_path = f'static/movies/{movie_name}'
    
    container = av.open(file_path)
    video_stream = next(s for s in container.streams if s.type == 'video')
    
    def generate():
        for packet in container.demux(video_stream):
            for frame in packet.decode():
                yield frame.to_image().tobytes()
    
    return StreamingResponse(generate(), media_type="video/mp4")
