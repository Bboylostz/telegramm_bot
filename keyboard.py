from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons_key = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='завтрак')],
    [KeyboardButton(text='обед')],
    [KeyboardButton(text='ужин')]
], resize_keyboard=True, input_field_placeholder='выберите прием пищи')

