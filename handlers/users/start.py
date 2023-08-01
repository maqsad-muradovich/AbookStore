from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.set_message_commands import choice_lan

from data.text import CHOOSE_LANGUAGE  #text data

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(text=f"{CHOOSE_LANGUAGE}", reply_markup=choice_lan)
