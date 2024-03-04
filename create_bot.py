from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import dotenv_values


config = dotenv_values(".env", encoding="utf-8")

TOKEN = config['TOKEN']
ID_CHANEL = config['ID_CHANEL']
ADMIN = config['ADMIN']

dp: Dispatcher = Dispatcher(storage=MemoryStorage())
bot = Bot(token=TOKEN, parse_mode='HTML')
