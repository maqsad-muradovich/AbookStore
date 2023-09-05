from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice_lan = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="EN", callback_data="en"),
            InlineKeyboardButton(text="RU", callback_data="ru"),
            InlineKeyboardButton(text="UZ", callback_data="uz")
        ]
    ]
)
