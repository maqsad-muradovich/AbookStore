from aiogram import types
from utils.Google_Translstor import translater
from loader import db, dp
from utils.InlineKeyboard import choice_lan


from data.text import CHOOSE_LANGUAGE
@dp.message_handler(commands=['language'])
async def change_the_language(message: types.Message):
    user_id = message.from_user.id
    lan = db.user_language(id_key=user_id)
    await message.answer(text=f"{translater(word=CHOOSE_LANGUAGE, first_l='uz',second_l=lan)}", reply_markup=choice_lan)
    await message.message.delete()