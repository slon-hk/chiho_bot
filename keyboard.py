from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

# UNDER BUTTON
keyboard_button = [[KeyboardButton(text="Ставка"), KeyboardButton(text="Внести часы")],
                   [KeyboardButton(text="Количество часов"), KeyboardButton(text="Все часы")]]
keyboard_main = ReplyKeyboardMarkup(keyboard=keyboard_button, resize_keyboard=True, input_field_placeholder="Выберете пункт меню!")

# Yes or No button
yes_no_button = [[KeyboardButton(text="Да"), KeyboardButton(text="Нет")]]
yes_no_btn_main = ReplyKeyboardMarkup(keyboard=yes_no_button, resize_keyboard=True, input_field_placeholder="Выберете пункт меню!")
