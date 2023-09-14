import sqlite3
import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.InlineKeyboard import choice_lan 
from loader import db, bot, dp

from data.text import CHOOSE_LANGUAGE, WELCOME #text data

from data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name_user = message.from_user.full_name
    id_user = message.from_user.id
    try:
        db.add_user(id=id_user, name=name_user)
    except:
        pass
    await message.answer(text=WELCOME)
    await message.answer(text=f"{CHOOSE_LANGUAGE}", reply_markup=choice_lan)
    count = db.count_user()[0]
    msg = f"{message.from_user.full_name}, bazaga qoshildi. \nBazada {count} ta foudalanuvchi bor."
    for admin in ADMINS:
        try:
            await bot.send_message(admin, msg)
        except Exception as err:
            logging.exception(err)
