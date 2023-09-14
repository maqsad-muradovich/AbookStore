from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from data.text import MENU_START, MENU_HELP, MENU_LIBRARY, MENU_ORDER, MENU_LANGUAGE
from utils.Google_Translstor import translater
from loader import db, dp



@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    user_id = message.from_user.id
    user_language = db.user_language(id_key=user_id)
    text = "Bot sozlamalari"
    secon_text = "Do'kon"
    text = (f"{translater(word=text, first_l='uz', second_l=user_language)}:",
    f"/start - {translater(word=MENU_START, first_l='uz', second_l=user_language)}",
    f"/help - {translater(word=MENU_HELP, first_l='uz', second_l=user_language)}",
    f"/language - {translater(word=MENU_LANGUAGE, first_l='uz', second_l=user_language)}",
    f"\n{translater(word=secon_text, first_l='uz', second_l=user_language)}:",
    f"/library - {translater(word=MENU_LIBRARY, first_l='uz', second_l=user_language)}",
    f"/order - {translater(word=MENU_ORDER, first_l='uz', second_l=user_language)}")
    await message.answer("\n".join(text))
