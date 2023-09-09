from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from data.text import MENU_START, MENU_HELP
from utils.Google_Translstor import translater
from loader import db

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            f"/start - {translater(word=MENU_START, first_l='uz', second_l=db.user_language(id=message.from_user.id))}",
            f"/help - {translater(word=MENU_HELP, first_l='uz', second_l=db.user_language(id=message.from_user.id))}")
    
    await message.answer("\n".join(text))
