from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bt_number_users: KeyboardButton = KeyboardButton(text='Новости')
bt_getting_all: KeyboardButton = KeyboardButton(text='Реклама')



kb_main_admin = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[bt_number_users, bt_getting_all]])