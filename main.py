from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse, Response
from fastapi.staticfiles import StaticFiles
from routers import reproductor
from os import getcwd, path

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(reproductor.router)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return FileResponse('static/templates/index.html')


# Ruta para servir archivos de películas
@app.get("/movies/{movie_name}")
async def read_movie(movie_name: str):
    file_path = f'static/movies/{movie_name}'
    
    # Usa StreamingResponse para reproducir el video 
    return StreamingResponse(open(file_path, mode="rb"), media_type="video/mp4")


############# Cosas o pasos que tengo que hacer si quiero hacer mi plataforma de streaming personal ################
# 1. Tratar que los videos se puedan pausar, adelantar, retroceder, subir volumen, bajar volumen, etc.
#### 2. Tratar de que los videos se puedan reproducir en distintas calidades
#### 3. Tratar de que los videos se puedan reproducir en distintos formatos
#### 4. Tratar de que los videos se puedan reproducir en distintos dispositivos
#### 5. Tratar de que los videos se puedan reproducir en distintos navegadores
#### 6. Tratar de que los videos se puedan reproducir en distintos sistemas operativos
# 7. poder renderizar una miniatura de la película, que esta se encuentra en mi catalogo pero que la miniatura lo haga de manera automatica
## osea que busque en internet la miniatura de la pelicula y la guarde en mi catalogo y la vaya cambiando cada cierto tiempo
# 8. poner un aparto de trailer, que se pueda ver el trailer de la pelicula lo que se me ocurre es 
# consumir una api de peliculas, no se de donde y hay sacar toda la informacion y poner el trailer del movie correcto, no se como puercas xd pero lo voy a intentar
# 9. Tengo muchas carpeta que tengo clasificadas todas mis peliculas entonces tengo que hacer un algoritmo que me las clasifique por genero, por año, por director, por actores, etc.
#### 10. Tengo que hacer un algoritmo que me recomiende peliculas, que me recomiende peliculas por genero, por año, por director, por actores, etc.
# 11. en cuanto a las series tengo que hacer como una especie de listado para las temporadas y los capitulos de cada temporada y que se puedan reproducir
# 12. Que al momento de casi terminar el capitulo de la seria este me recomiende el siguiente capitulo
# 13. Que al momento de casi terminar la pelicula me recomiende otra pelicula
# 14. Las peliculas y serias que ya haya visto que no me las recomiende de nuevo y los vaya guardando en una lista de peliculas y serias vistas

