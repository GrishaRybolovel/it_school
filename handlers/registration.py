from aiogram import types, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command

from keyboards.keyboards import keyboard
from database.db import insert_user

class Registration(StatesGroup):
    name = State()
    phone_number = State()


async def start_command(message: types.Message, state: FSMContext):
    await message.answer("Добро пожаловать! Введите имя:", reply_markup=keyboard)
    await state.set_state(Registration.name)

async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Хорошо! Теперь номер телефона:", reply_markup=keyboard)
    await state.set_state(Registration.phone_number)

async def process_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)

    user_data = await state.get_data()
    name = user_data['name']
    phone_number = user_data['phone_number']
    db = Database()
    await db.connect()
    try:
        user_id = await db.insert_user(name, phone_number)
        await message.answer(
            f"Записал вас к себе в базу! Ваш ID: '{user_id}'")
    except Exception as e:
        await message.answer(f"An error occurred: {e}")

    await db.disconnect()

    await message.answer(f"Спасибо за регистрацию, {name}")

    await state.clear()

async def handle_callback_query(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == 'cancel_registration':
        await state.clear()
        await callback_query.message.answer('Регистрация отменена.')
        await callback_query.answer()

def register_handlers(dp: Dispatcher):
    dp.message.register(start_command, Command("start"))
    dp.message.register(process_name, Registration.name)
    dp.message.register(process_phone_number, Registration.phone_number)
    dp.callback_query.register(handle_callback_query)
