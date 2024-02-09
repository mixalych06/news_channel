from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import select, func, update, insert

from data.models import Base
from create_bot import config
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

dbname = config['dbname']
host = config['host']
user = config['user']
password = config['password']

engine = create_async_engine(f'postgresql+asyncpg://{user}:{password}@{host}/{dbname}')  # , echo=True
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)


async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        return session


async def add_news(news: list, latest_news, model):
    session: AsyncSession = await get_async_session()
    for d, l in news[::-1]:
        stmt = insert(model).values(date=datetime.now(), title=d, link=l)
        await session.execute(stmt)
        await session.commit()


async def get_max_date(model):
    session = await get_async_session()
    stmt = select(model.title, model.link).where(model.date == select(func.max(model.date)))
    result = await session.execute(stmt)
    result = result.first()
    await session.commit()
    return result


async def get_min_date(model):
    session = await get_async_session()
    stmt = select(model).where(model.completed == False).order_by(model.date)
    result = await session.execute(stmt)
    result = result.scalar()
    await session.commit()
    return result


async def update_completed(id_news, model):
    session = await get_async_session()
    stmt = update(model).where(model.id == id_news).values(completed=True)
    await session.execute(stmt)
    await session.commit()
