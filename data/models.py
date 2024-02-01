from datetime import datetime

from sqlalchemy import String, Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass

class News_ASN24(Base):
    __tablename__ = 'news_asn24'

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime] = mapped_column()
    title: Mapped[str] = mapped_column()
    link: Mapped[str] = mapped_column()
    completed: Mapped[bool] = mapped_column(Boolean(), default=False)

class News_AmurLifeNews(Base):
    __tablename__ = 'news_amurlife'

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime] = mapped_column()
    title: Mapped[str] = mapped_column()
    link: Mapped[str] = mapped_column()
    completed: Mapped[bool] = mapped_column(Boolean(), default=False)

class News_AmurInfo(Base):
    __tablename__ = 'news_amurinfo'

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime] = mapped_column()
    title: Mapped[str] = mapped_column()
    link: Mapped[str] = mapped_column()
    completed: Mapped[bool] = mapped_column(Boolean(), default=False)



    # def __str__(self):
    #     return f'{self.id, self.title, self.description, self.completed}'