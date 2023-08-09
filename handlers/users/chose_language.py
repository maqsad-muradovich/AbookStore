from aiogram import types
from loader import dp
from data.text import LANGUAGE
from data.data_base import insert_user_id

@dp.callback_query_handler(text="EN")
async def language(call: types.CallbackQuery):
    await call.message.answer(text=f"{LANGUAGE}, {call.message.message_id}")
    # await insert_user_id(call.message.from_user.id, call.message)