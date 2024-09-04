from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_calc = KeyboardButton('Начать подсчет')


kb = ReplyKeyboardMarkup(resize_keyboard=True)

kb.add(btn_calc)
