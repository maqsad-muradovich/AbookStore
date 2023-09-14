from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from utils.Google_Translstor import translater
from loader import db, dp, bot
from data.config import ADMINS



class Form(StatesGroup):
    name = State()
    name_author = State()
    year = State()


class order_book():
    title = str()
    author = str()
    year_of_issue = str()
    user_id = None
    user_fullname = None


book = order_book()


@dp.message_handler(commands='order')
async def bot_help(message: types.Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer(text="Book title")
    book.user_id = message.from_user.id
    book.user_fullname = message.from_user.full_name


@dp.message_handler(state=Form.name)
async def book_title(message: types.Message, state: FSMContext):
    await state.set_state(Form.name_author)
    book.title = message.text
    await message.answer(text="Book author: ")


@dp.message_handler(state=Form.name_author)
async def book_author(message: types.Message, state: FSMContext):
    await state.set_state(Form.year)
    book.author = message.text
    await message.answer(text="Book release date: ")


@dp.message_handler(state=Form.year)
async def book_year(message: types.Message, state: FSMContext):
    book.year_of_issue = message.text
    await state.finish()
    await message.answer("Haridingiz uchun rahmat")
    txt = (
        f"Book title: {book.title}",
        f"Book author: {book.author}",
        f"Book year: {book.year_of_issue}\n",
        f"User: {book.user_fullname}",
        f"User id: {book.user_id}"
    )
    await bot.send_message(chat_id=-918950367, text="\n".join(txt))
