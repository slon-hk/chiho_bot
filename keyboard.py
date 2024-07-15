import logging
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

# Set up logging
logger = logging.getLogger(__name__)

# UNDER BUTTON
# Define the main keyboard buttons
keyboard_button = [
    [KeyboardButton(text="Ставка"), KeyboardButton(text="Внести часы")],
    [KeyboardButton(text="Количество часов"), KeyboardButton(text="Все часы")]
]

# Create the main keyboard layout
keyboard_main = ReplyKeyboardMarkup(
    keyboard=keyboard_button, 
    resize_keyboard=True, 
    input_field_placeholder="Выберете пункт меню!"
)

logger.info("Main keyboard created with buttons: %s", keyboard_button)

# Yes or No button
# Define the yes/no keyboard buttons
yes_no_button = [
    [KeyboardButton(text="Да"), KeyboardButton(text="Нет")]
]

# Create the yes/no keyboard layout
yes_no_btn_main = ReplyKeyboardMarkup(
    keyboard=yes_no_button, 
    resize_keyboard=True, 
    input_field_placeholder="Выберете пункт меню!"
)

logger.info("Yes/No keyboard created with buttons: %s", yes_no_button)