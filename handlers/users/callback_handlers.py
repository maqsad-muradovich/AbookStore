from aiogram.types import Message, CallbackQuery
from loader import dp, bot, db
from data.text import LANGUAGE
from utils.Google_Translstor import translater


@dp.callback_query_handler()
async def language(call: CallbackQuery):
    if call.data == "en":
        db.update_user_language(id=call.from_user.id, language='en')
        lan = db.user_language(id_key=call.from_user.id)
        await bot.send_message(chat_id=call.from_user.id, text=translater(word=LANGUAGE, first_l='uz', second_l='en'))
    elif call.data == "ru":
        db.update_user_language(id=call.from_user.id, language='ru')
        lan = db.user_language(id=call.from_user.id)
        await bot.send_message(chat_id=call.from_user.id, text=translater(word=LANGUAGE, first_l='uz', second_l='ru'))
    else:
        db.update_user_language(id=call.from_user.id, language='uz')
        await bot.send_message(chat_id=call.from_user.id, text=LANGUAGE)

        await call.message.delete()
