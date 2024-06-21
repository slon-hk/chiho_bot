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

bot = Bot(token="")
router = Router()
storage = MemoryStorage()

class FSMFillForm(StatesGroup):
    fill_rate = State()
    fill_houre = State()

#Start message and registration
@router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("""Привет это бот для подсчета часов и зарплаты!\n
                            Для начала внесите свою ставку, нажав на кнопку 'ставка'\n
                            А потом можете вносить отработанные часы с помощбю кнопки 'Внести часы'\n
                            Чтобы посмотреть все отработанные часы за месяц нажмите на кнопку 'Количество часов\n\n
                            Приятного пользования!'""", reply_markup=kb.keyboard_main)
    db.start()
    
# Обработчик для команды "Ставка"
@router.message(F.text == "Ставка")
async def fill_rate_start(message: types.Message, state: FSMContext):
    await message.answer(text='Введите свою ставку')
    await state.set_state(FSMFillForm.fill_rate)

# Обработчик для состояния fill_rate
@router.message(StateFilter(FSMFillForm.fill_rate))
async def fill_rate(message: types.Message, state: FSMContext):
    rate = message.text
    if rate.isdigit():
        rate = int(rate)
        db.fill_rate(tg_id=message.from_user.id, rate=rate)
        await message.answer(text="✅")
        await state.clear()
    else:
        await message.answer(text="Это не является числом, введите число")

# Обработчик для команды "Внести часы"
@router.message(F.text == "Внести часы")
async def send_voice_message(message: types.Message, state: FSMContext):
    await message.answer(text="Внесите количество часов, которые вы отработали сегодня")
    await state.set_state(FSMFillForm.fill_houre)

# Обработчик для состояния fill_houre
@router.message(StateFilter(FSMFillForm.fill_houre))
async def get_houre(message: types.Message, state: FSMContext):
    houre = message.text
    try:
        houre = float(houre)
        db.fill_houre(tg_id=message.from_user.id, houre=houre)
        await message.answer(text="✅")
        await state.clear()
    except ValueError:
        await message.answer(text="Это не является числом, введите число")

@router.message(F.text == "Количество часов")
async def get_houre(message: types.Message):
    await message.answer(db.get_houre(tg_id=message.from_user.id))