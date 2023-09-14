from aiogram import types
from data.text import MENU_START, MENU_HELP, MENU_LIBRARY, MENU_ORDER, MENU_LANGUAGE
from utils.Google_Translstor import translater


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand(command="start", description=translater(word=MENU_START, first_l='uz', second_l='en')),
            types.BotCommand(command="help", description=translater(word=MENU_HELP, first_l='uz', second_l='en')),
            types.BotCommand(command="library", description=translater(word=MENU_LIBRARY, first_l='uz', second_l='en')),
            types.BotCommand(command="order", description=translater(word=MENU_ORDER, first_l='uz', second_l='en')),
            types.BotCommand(command="language", description=translater(word=MENU_LANGUAGE, first_l='uz', second_l='en'))
        ]
    )

