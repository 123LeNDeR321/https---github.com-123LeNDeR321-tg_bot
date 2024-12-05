from aiogram import* #роутер
from aiogram.client.bot import DefaultBotProperties
from aiogram.types import* #команды
from aiogram.filters import*  #фильтры
from config import TOKEN, OWNER_ID  #токен бота
from game import* #список игр
from command import* #команды бота
from config import*
from aiogram.enums import ParseMode
TOKEN_API = TOKEN

bot = Bot(token=TOKEN_API, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):

    bot_commands = [
        BotCommand(command=help_command, description="Помощь с функционалом бота"),
        BotCommand(command=start_command, description="Запустить"),
        BotCommand(command=svo_command, description="Пойти на СВО"),
        BotCommand(command=zov_command, description="Я услышал зов?"),
        BotCommand(command=game_command, description="Выведет игры по жанру, который вы укажете")
    ]
    
    await bot.set_my_commands(bot_commands)
    await message.reply("Привет, я Svой, не бойся, что-бы узнать меня получше, напиши /help")

@router.message(Command(zov_command))
async def cmd_zov(message: Message):
    await message.reply("<b>Слышу зов, ебать азов</b>")

@router.message(Command(help_command))
async def cmd_help(message: Message):
    await message.reply(f"<b>Команды:\n/{start_command}\n/{help_command}\n/{zov_command}\n/{svo_command}\n{game_command}\nя улучшаюсь, поэтому этот список увеличится :)</b>")

@router.message(Command(svo_command))
async def cmd_svo(message: Message):
    await message.answer("<b>СВО, ГОЙДА БРАТЬЯ, Я ВАС ЛЮБЛЮ</b>")
    # await bot.send_audio(message.from_user.id, open("1-Татьяна-Куртукова-Матушка-J84Y9D.flac", "r"), performer = "Performer", title = "Title")
    
keys = ', '.join(list(game_dictionary.keys())) # список игры

@router.message(Command(game_command))
async def cmd_game(message: Message):
    await message.answer(f"<b>Напиши жанр который тебе нравится из приведённых:\n{keys}</b>")

@router.message()
async def get_start(message: Message):
    keys = ', '.join(list(game_dictionary.keys()))
    
    if message.text.lower() in game_dictionary.keys():
        await message.reply(f"Возможно тебе понравятся эти игры:\n<b>{', '.join(game_dictionary[message.text.lower()])}</b>")
    elif message.text.lower() == "иди нахуй":
        await message.reply("<b>Ты чё падаль, попутал мальца?</b>")
    else:
        await message.reply(f"<b>Хай {message.from_user.first_name}, не забывай, что у меня есть доступ к тоему IP :).</b>")
 




