from aiogram import types
from loader import dp
from data.text import LANGUAGE
from data.data_base import insert_info


@dp.callback_query_handler(text="EN")
async def language(call: types.CallbackQuery):
    await call.message.answer(text=f"{LANGUAGE}")
    await insert_info(1, call.message)