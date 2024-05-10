import asyncio

from create_bot import bot, dp

from handlers import h_admin
from data.orm import create_table
from utils.parsers import check_news_amur
from utils.parsers import sends_news_amur


async def create_task():
    task1 = asyncio.create_task(sends_news_amur(120))


async def main() -> None:
    await create_table()
    dp.include_router(h_admin.router)
    await bot.delete_webhook(drop_pending_updates=True)

    await create_task()

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
