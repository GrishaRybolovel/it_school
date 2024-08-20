from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_calc = KeyboardButton('Начать подсчет')


kb = ReplyKeyboardMarkup(resize_keyboard=True)

kb.add(btn_calc)


keyboard_city = ReplyKeyboardMarkup()
keyboard_city.add("Казань")
keyboard_city.add("Нижнекамск")
keyboard_city.add("Тольятти")
keyboard_city.add("Москва")
keyboard_city.add("Самара")
keyboard_city.add("Назад")