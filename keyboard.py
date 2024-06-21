from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

# UNDER BUTTON
keyboard_button = [[KeyboardButton(text="Ставка"), KeyboardButton(text="Внести часы")],
				   [KeyboardButton(text="Количество часов")]]
keyboard_main = ReplyKeyboardMarkup(keyboard=keyboard_button, resize_keyboard=True, input_field_placeholder="Выберете пункт меню!")
