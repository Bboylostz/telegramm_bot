import asyncio
import logging
import sys
from aiogram import types, F
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, html
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from sulguk import SULGUK_PARSE_MODE

from config import SEEN_USERS, cursor
from database import Database
from keyboard import buttons_key
from recipes import db
from config import db_connection

bot = Bot(token='8127289280:AAExatCe0dW7qMMG1LTUWeiitZojwOd_yPI')
dp = Dispatcher()
seen_users = set()
db = Database('recipes.db')

@dp.message(F.text == 'завтрак')
async def catalog(message: Message):
    await message.answer('вы выбрали завтрак')

@dp.message(F.text == 'обед')
async def catalog(message: Message):
    await message.answer('вы выбрали обед')

@dp.message(F.text == 'ужин')
async def catalog(message: Message):
    await message.answer('вы выбрали ужин')


from config import db_connection


@dp.message()
async def handle_recipe_request(message: types.Message):
    recipe_type = message.text.lower().strip()

    cursor.execute('SELECT * FROM recipes WHERE type = ?', (recipe_type,))
    recipe = cursor.fetchone()

    if recipe:
        name, _, image_path, ingredients, instructions = recipe
        await message.answer_photo(image_path, caption=f"{recipe_type.upper()} РЕЦЕПТ:")
        await message.answer(f"Название: {name}\nИнгредиенты: {ingredients}\nИнструкции:\n{instructions}")
    else:
        await message.answer("К сожалению, у меня нет рецептов для этого типа.")


async def handle_main_menu(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton(text="Завтрак", callback_data="breakfast"),
        InlineKeyboardButton(text="Обед", callback_data="lunch"),
        InlineKeyboardButton(text="Ужин", callback_data="dinner")
    ]
    keyboard.add(*buttons)
    await message.answer("Выберите время приема пищи:", reply_markup=keyboard)
@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    html_content = f"Hello, {message.from_user.full_name}!"
    await message.answer(text=html_content, reply_markup=buttons_key)

@dp.message()
async def echo_message(message: types.Message):
    if message.from_user.id not in SEEN_USERS:
        SEEN_USERS.add(message.from_user.id)
        html_content = f"<b>Добро пожаловать в бот , {message.from_user.first_name}!</b>\n\nпожалуйсто выберите команду:\n/start - Просмотреть меню\n/help - помощь\n"
        try:
            result = html.parse(html_content)
            await message.answer(result.text, parse_mode=SULGUK_PARSE_MODE)
        except Exception as e:
            await message.answer(
                f"Добро пожаловать в бот , {message.from_user.first_name}!\n\nпожалуйсто выберите команду:\n/start - Просмотреть меню\n/help - помощь\n")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
