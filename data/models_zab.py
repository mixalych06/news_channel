from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped, mapped_column

from data.models import Base


class News_Chita(Base):
    __tablename__ = 'news_chita'

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime] = mapped_column()
    title: Mapped[str] = mapped_column()
    link: Mapped[str] = mapped_column()
    completed: Mapped[bool] = mapped_column(Boolean(), default=False)


class News_ZabNews(Base):
    __tablename__ = 'news_zabnews'

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime] = mapped_column()
    title: Mapped[str] = mapped_column()
    link: Mapped[str] = mapped_column()
    completed: Mapped[bool] = mapped_column(Boolean(), default=False)


class News_Zab(Base):
    __tablename__ = 'news_zab'

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime] = mapped_column()
    title: Mapped[str] = mapped_column()
    link: Mapped[str] = mapped_column()
    completed: Mapped[bool] = mapped_column(Boolean(), default=False)
