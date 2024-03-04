from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command

from keyboards.kb_admin import kb_main_admin
from utils.parsers import pars_amur_life

router: Router = Router()
# router.message.filter(AdmFilter())  # применяем ко всем хендлерам фильтр на админа

@router.message(CommandStart())
async def start_admin(msg: types.Message):
    await msg.answer(f"Hello, {msg.from_user.full_name}!")
    await msg.answer(text=f'Привет {msg.from_user.id}')



@router.message()
async def message(msg: types.Message):
    await msg.reply('ljhlkn;l')
