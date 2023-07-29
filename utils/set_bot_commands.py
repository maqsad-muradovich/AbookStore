from aiogram import types
from data.text import MENU_START, MENU_HELP, MENU_LIBRARY, MENU_ORDER, MENU_PROFILE


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", MENU_START),
            types.BotCommand("help", MENU_HELP),
            types.BotCommand("library", MENU_LIBRARY),
            types.BotCommand("order", MENU_ORDER),
            types.BotCommand("myprofile", MENU_PROFILE)
        ]
    )
