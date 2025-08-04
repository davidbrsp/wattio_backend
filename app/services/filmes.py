from repository.filmes import get_filme

class FilmesService:
    def __init__(self):
        self.filmes = [{"title": "Inception"}, {"title": "Interstellar"}]

    async def get_filmes(self):
        return self.filmes

    async def get_filme(self, id: int):
        return get_filme(id)
        # return next((filme for filme in self.filmes if filme["id"] == id), None)

    async  def create_filme(self, filme: dict):
        self.filmes.append(filme)
        return filme
