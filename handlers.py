import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, FSInputFile
from aiogram.filters.command import Command
from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize)
import asyncio

import keyboard as kb
import db

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token="6587114212:AAEQDJHhz3dD7SnXiRfAg43qgV_HLOxdKK8")
router = Router()
storage = MemoryStorage()

class FSMFillForm(StatesGroup):
    fill_rate = State()
    fill_houre = State()
    yes_no_btn = State()

# Start message and registration
@router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    logger.info("CommandStart received from user: %s", message.from_user.id)
    await message.answer("""Привет это бот для подсчета часов и зарплаты!\nДля начала внесите свою ставку, нажав на кнопку 'ставка'\nА потом можете вносить отработанные часы с помощбю кнопки 'Внести часы'\nЧтобы посмотреть все отработанные часы за месяц нажмите на кнопку 'Количество часов\n\nПриятного пользования!'""", reply_markup=kb.keyboard_main)
    db.start()

# Handler for "Ставка" command
@router.message(F.text == "Ставка")
async def fill_rate_start(message: types.Message, state: FSMContext):
    logger.info("Received 'Ставка' command from user: %s", message.from_user.id)
    if db.user_exists(message.from_user.id) == False:
        await message.answer(text='Введите свою ставку')
        await state.set_state(FSMFillForm.fill_rate)
        logger.info("Prompting user %s to enter their rate", message.from_user.id)
    else:
        await message.answer(text="Вы уже внесли свою ставку.\nХотите изменить ставку?", reply_markup=kb.yes_no_btn_main)
        await state.set_state(FSMFillForm.yes_no_btn)
        logger.info("User %s already has a rate, asking if they want to change it", message.from_user.id)

# Handler for fill_rate state
@router.message(StateFilter(FSMFillForm.fill_rate))
async def fill_rate(message: types.Message, state: FSMContext):
    rate = message.text
    if rate.isdigit():
        rate = int(rate)
        db.fill_rate(tg_id=message.from_user.id, rate=rate)
        await message.answer(text="✅",  reply_markup=kb.keyboard_main)
        await state.clear()
        logger.info("User %s set their rate to %d", message.from_user.id, rate)
    else:
        await message.answer(text="Это не является числом, введите число")
        logger.warning("User %s entered an invalid rate: %s", message.from_user.id, rate)

@router.message(F.text == "Да", StateFilter(FSMFillForm.yes_no_btn))
async def change_rate(message: types.Message, state: FSMContext):
    db.delete_user(message.from_user.id)
    await message.answer(text="Введите ставку", reply_markup=kb.keyboard_main)
    await state.set_state(FSMFillForm.fill_rate)
    logger.info("User %s chose to change their rate", message.from_user.id)

# Handler for "Внести часы" command
@router.message(F.text == "Внести часы")
async def send_voice_message(message: types.Message, state: FSMContext):
    await message.answer(text="Внесите количество часов, которые вы отработали сегодня")
    await state.set_state(FSMFillForm.fill_houre)
    logger.info("Prompting user %s to enter worked hours", message.from_user.id)

# Handler for fill_houre state
@router.message(StateFilter(FSMFillForm.fill_houre))
async def get_houre(message: types.Message, state: FSMContext):
    houre = message.text
    try:
        houre = float(houre)
        db.fill_houre(tg_id=message.from_user.id, houre=houre)
        await message.answer(text="✅")
        await state.clear()
        logger.info("User %s entered worked hours: %f", message.from_user.id, houre)
    except ValueError:
        await message.answer(text="Это не является числом, введите число")
        logger.warning("User %s entered an invalid number of hours: %s", message.from_user.id, houre)

@router.message(F.text == "Количество часов")
async def get_houre(message: types.Message):
    logger.info("User %s requested total hours for current month", message.from_user.id)
    await message.answer(db.get_hours(tg_id=message.from_user.id))

@router.message(F.text == "Все часы")
async def get_houre(message: types.Message):
    logger.info("User %s requested all worked hours", message.from_user.id)
    await message.answer(db.all_stats(tg_id=message.from_user.id))
