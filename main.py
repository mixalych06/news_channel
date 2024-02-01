import asyncio

from create_bot import bot, dp

from handlers import h_admin
from data.orm import create_table
from utils.parsers import start_checks_for_news_amur_life, start_checks_for_news_asn24, start_checks_for_news_amurinfo
from utils.parsers import sends_news



async def main() -> None:
    dp.include_router(h_admin.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await create_table()
    task1 = asyncio.create_task(start_checks_for_news_amur_life(35))
    task2 = asyncio.create_task(start_checks_for_news_asn24(35))
    task3 = asyncio.create_task(start_checks_for_news_amurinfo(35))
    task4 = asyncio.create_task(sends_news(10))
    await task1
    await task2
    await task3
    await task4

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
