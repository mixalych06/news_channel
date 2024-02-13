import asyncio

from create_bot import bot, dp

from handlers import h_admin
from data.orm import create_table
from utils.parsers import start_checks_for_news_amur_life, start_checks_for_news_asn24, start_checks_for_news_amurinfo
from utils.parsers import sends_news


async def create_task():

    task1 = asyncio.create_task(start_checks_for_news_amur_life(70))
    task2 = asyncio.create_task(start_checks_for_news_asn24(80))
    task3 = asyncio.create_task(start_checks_for_news_amurinfo(90))
    task4 = asyncio.create_task(sends_news(60))

async def main() -> None:

    dp.include_router(h_admin.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await create_table()
    await create_task()
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())
