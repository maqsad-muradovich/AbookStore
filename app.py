from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)


# Traceback (most recent call last):
#   File "/home/user/Документы/AbookStore_2/app.py", line 4, in <module>
#     import middlewares, filters, handlers
#   File "/home/user/Документы/AbookStore_2/handlers/__init__.py", line 2, in <module>
#     from . import users
#   File "/home/user/Документы/AbookStore_2/handlers/users/__init__.py", line 3, in <module>
#     from . import start
#   File "/home/user/Документы/AbookStore_2/handlers/users/start.py", line 3, in <module>
#     from AbookStore_2.utils.mes_commands import choice_lan 
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ModuleNotFoundError: No module named 'AbookStore_2'
                                                     