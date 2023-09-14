from aiogram import types
from utils.Google_Translstor import translater

from loader import dp, db, bot

# @dp.message_handler(content_types='sticker')
# async def bot_echo(message: types.Message):
#     await message.answer(message.sticker.file_id)

# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(text="🗿")
    await message.answer(text=translater(word='Men sizni tushunmayapman',first_l='uz',second_l=db.user_language(id_key=message.from_user.id)))
    await bot.send_message(chat_id=-918950367, text="Hellomaleykum")