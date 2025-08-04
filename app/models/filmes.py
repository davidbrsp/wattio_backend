from sqlalchemy.orm import Mapped, mapped_column
from . import Base

class Filme(Base):
    __tablename__ = "filmes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    titulo: Mapped[str] 
    descricao: Mapped[str]
    ano: Mapped[int]
    genero: Mapped[str]
    diretor: Mapped[str]
    atores: Mapped[list[str]]
    url_trailer: Mapped[str]

