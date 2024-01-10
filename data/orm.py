import typing

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from dotenv import dotenv_values

from data.models import Base


config = dotenv_values("../.env", encoding="utf-8")

dbname = config['dbname']
host = config['host']
user = config['user']
password = config['password']

engine = create_async_engine(f'postgresql+asyncpg://{user}:{password}@{host}/{dbname}')
async_session_maker = async_sessionmaker(engine)


async def create_table():
    async with engine.begin() as conn:
        await conn.run_sunc(Base.metadata.create_all)


async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session