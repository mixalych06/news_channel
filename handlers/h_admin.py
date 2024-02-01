from aiogram import Router, types, F
from aiogram.filters import CommandStart

from create_bot import bot, ID_CHANEL
from keyboards.kb_admin import kb_main_admin
from utils.parsers import pars_amur_life

router: Router = Router()
# router.message.filter(AdmFilter())  # применяем ко всем хендлерам фильтр на админа

@router.message(CommandStart())
async def start_admin(msg: types.Message):
    await msg.answer(text=f'Привет {msg.from_user.id}', reply_markup=kb_main_admin)

@router.message(F.text == 'Новости')
async def all_news(msg: types.Message):
    '''
    Получает из БД неопубликованные сообщения и отправляет их в канал и
    ставит флаг в БД что новость отправлена
    :param msg:
    :return:
    '''
    news = pars_amur_life()
    for d, n in sorted(news.items()):

        await bot.send_message(chat_id=ID_CHANEL,
                               text=f'{d}\n'
                                    f'{n[1]}')

