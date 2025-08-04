from app.models.filmes import Filmes as FilmesDBModel
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_filme(db_session: AsyncSession, filme_id: int):
    filme = (await db_session.scalars(select(FilmesDBModel).where(FilmesDBModel.id == filme_id))).first()
    if not filme:
        filme = {}
    return filme
    # if not user:
    #     raise HTTPException(status_code=404, detail="User not found")
    # return user


async def get_user_by_email(db_session: AsyncSession, email: str):
    return (await db_session.scalars(select(UserDBModel).where(UserDBModel.email == email))).first()