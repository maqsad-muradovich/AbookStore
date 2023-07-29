from aiogram import types
from loader import dp
from data.text import LANGUAGE


@dp.callback_query_handler(text="EN")
async def language(call: types.CallbackQuery):
    await call.message.answer(text=f"{LANGUAGE}")