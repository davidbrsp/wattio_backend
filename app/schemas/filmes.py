from pydantic import AnyUrl, BaseModel, ConfigDict

class Filme(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    titulo: str
    descricao: str
    ano: int
    genero: str
    diretor: str
    atores: list[str]
    url_trailer: AnyUrl
