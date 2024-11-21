from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message
import asyncio
import logging
from config import TOKEN  #токен бота

TOKEN_API = TOKEN


async def get_start(message: Message):
    await message.reply(f"<b>Хай {message.from_user.first_name}. Прости за прошлое.</b>")



async def start():
    bot = Bot(token=TOKEN_API, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.message.register(get_start)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
    
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        print("Exit")
        