from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from data.text import MENU_START, MENU_HELP

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            f"/start - {MENU_START}",
            f"/help - {MENU_HELP}")
    
    await message.answer("\n".join(text))
