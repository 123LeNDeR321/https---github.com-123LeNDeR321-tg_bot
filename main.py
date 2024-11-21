from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message
import asyncio
import logging
from config import TOKEN, OWNER_ID  #токен бота

TOKEN_API = TOKEN

bot = Bot(token=TOKEN_API, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()
async def get_start(message: Message):
    if "svo" in message.text.lower():
        await message.reply(f"<b>ZOV\nZOV\nZOV</b>")
    else:
        await message.reply(f"<b>Хай {message.from_user.first_name}. Прости за прошлое.</b>")
    
async def bot_start():
    await bot.send_message(chat_id=OWNER_ID, text="Бот запущен")

async def bot_stop():
    await bot.send_message(chat_id=OWNER_ID , text="<b>Бот остановлен</b>")


async def start():
    
    dp.startup.register(bot_start)
    dp.shutdown.register(bot_stop)
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
        