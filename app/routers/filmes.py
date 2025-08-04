from fastapi import APIRouter
from services.filmes import FilmesService

router = APIRouter(
    prefix="/filmes",
    tags=["filmes"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_filmes():
    return await FilmesService().get_filmes()

@router.get("/{id}")
async def read_filme(id: int):
    return await FilmesService().get_filme(id)

@router.post("/")
async def create_filme(filme: dict):
    return await FilmesService().create_filme(filme)
