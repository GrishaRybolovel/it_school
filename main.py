import asyncio
from handlers.registration import register_handlers

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

# Initialize storage, bot, and dispatcher
storage = MemoryStorage()
bot = Bot(token='7479680326:AAHGXy8wxDe92qI9e9de1eBoyFjgPskbMPI')
dp = Dispatcher(storage=storage)


async def on_startup(dp: Dispatcher):
    print('Бот вышел в онлайн!')


async def main():
    register_handlers(dp)
    await dp.start_polling(bot, skip_updates=True, on_startup=on_startup)


if __name__ == '__main__':
    asyncio.run(main())
