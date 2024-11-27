from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import*
from config import TOKEN, OWNER_ID  #токен бота
from game import*
from command import*
import asyncio
import logging

TOKEN_API = TOKEN

bot = Bot(token=TOKEN_API, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply("Привет, я Svой, не бойся, что-бы узнать меня получше, напиши /help")

@dp.message(Command(zov_command))
async def cmd_zov(message: Message):
    await message.reply("<b>Слышу зов, ебать азов</b>")

@dp.message(Command(help_command))
async def cmd_help(message: Message):
    await message.reply(f"<b>Команды:\n/{start_command}\n/{help_command}\n/{zov_command}\n/{svo_command}\nя улучшаюсь, поэтому этот список увеличится :)</b>")

@dp.message(Command(svo_command))
async def cmd_svo(message: Message):
    await message.answer("<b>СВО, ГОЙДА БРАТЬЯ, Я ВАС ЛЮБЛЮ</b>")
    
keys = ', '.join(list(game_dictionary.keys()))

@dp.message(Command(game_command))
async def cmd_game(message: Message):
    await message.answer(f"<b>Напиши жанр который тебе нравится из приведённых:\n{keys}</b>")

async def get_start(message: Message):
    keys = ', '.join(list(game_dictionary.keys()))

    if message.text.lower() in game_dictionary.keys():
        await message.reply(f"Возможно тебе понравятся эти игры:\n<b>{', '.join(game_dictionary[message.text.lower()])}</b>")
    elif message.text.lower() == "иди нахуй":
        await message.reply("<b>Ты чё падаль, попутал мальца?</b>")
    else:
        await message.reply(f"<b>Хай {message.from_user.first_name}, не забывай, что у меня есть доступ к тоему IP :).</b>")
    
async def bot_start():
    await bot.send_message(chat_id=OWNER_ID, text="<b>Бот запущен</b>")

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
        