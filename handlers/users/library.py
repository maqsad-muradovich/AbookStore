from aiogram import types
from loader import dp, db
from data.text import LIBRARY
from utils.Google_Translstor import translater


@dp.message_handler(commands='library')
async def library(message: types.Message):
    id = message.from_user.id
    await message.answer_sticker('CAACAgQAAxkBAAIEcGT9hU-N6EnUKY1fvKa40yKjmiViAAJkCgACbGPIU6_t19rFXU9sMAQ')
    await message.answer(text=translater(word=LIBRARY, first_l='uz', second_l=db.user_language(id_key=id)))