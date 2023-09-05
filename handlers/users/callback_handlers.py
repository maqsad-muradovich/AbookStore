from aiogram.types import Message, CallbackQuery
from loader import dp, bot
from data.text import LANGUAGE
from data.data_base import insert_user_id
from utils.Yandex_Translstor import translater



@dp.callback_query_handler(text="en")
async def language(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=f"{translater(LANGUAGE,'uz','en')}")



@dp.callback_query_handler(text="ru")
async def language(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=f"{translater(LANGUAGE,'uz','ru')}")



@dp.callback_query_handler(text="uz")
async def language(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=LANGUAGE)