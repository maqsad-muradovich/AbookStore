from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice_lan = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="EN", callback_data="EN"),
            InlineKeyboardButton(text="RU", callback_data="RU"),
            InlineKeyboardButton(text="UZ", callback_data="UZ")
        ]
    ]
)
