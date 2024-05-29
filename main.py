import asyncio

from create_bot import bot, dp

from handlers import h_admin
from data.orm import create_table
from utils.parsers import check_news_amur
from utils.parsers import sends_news_amur

from apscheduler.schedulers.asyncio import AsyncIOScheduler


async def create_task():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(sends_news_amur, 'interval', seconds=180)
    scheduler.start()


async def main() -> None:
    await create_table()
    dp.include_router(h_admin.router)
    await bot.delete_webhook(drop_pending_updates=True)

    await create_task()

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
