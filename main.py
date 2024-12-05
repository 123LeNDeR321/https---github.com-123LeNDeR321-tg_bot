from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from config import TOKEN, OWNER_ID  #токен бота
from handlers import router
import asyncio
import logging

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()

async def bot_start():
    await bot.send_message(chat_id=OWNER_ID, text="<b>Бот запущен</b>")

async def bot_stop():
    await bot.send_message(chat_id=OWNER_ID , text="<b>Бот остановлен</b>")

async def start():
    dp.include_router(router)
    dp.startup.register(bot_start)
    dp.shutdown.register(bot_stop)   
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
        