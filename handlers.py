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
    await message.answer("Привет это бот для подсчета часов и зарплаты", reply_markup=kb.keyboard_main)
    db.start()
    
@router.message(F.text == "Ставка")
async def fill_rate(message: types.Message, state: FSMContext):
    await message.answer(text='Введите свою ставку')
    await state.set_state(FSMFillForm.fill_rate)
@router.message(StateFilter(FSMFillForm.fill_rate))
async def fill_rate(message: types.Message, state: FSMContext):
    rate = message.text()
    if rate.content_type == 'text':
        try:
            rate = int(rate)
            db.fill_rate(tg_id=message.from_user.id, rate=rate)
            await message.answer(text="✅")
            await state.clear()
        except TypeError or ValueError:
            await message.answer(text="Это не являеться числом, введите число")
            


@router.message(F.text == "Внести часы")
async def send_voice_message(message: types.Message, state: FSMContext):
    await message.answer(text = "Внесите количество часов которые вы отработали сегодня")
    await state.set_state(FSMFillForm.fill_houre)

@router.message(StateFilter(FSMFillForm.fill_houre))
async def get_houre(message: types.Message, state: FSMContext):
    try:
        db.fill_houre(tg_id=message.from_user.id, houre=float(message.text))
        await message.answer(text="✅")
        await state.clear()
    except TypeError or ValueError:
            await message.answer(text="Это не являеться числом, введите число")

@router.message(F.text == "Количество часов")
async def get_houre(message: types.Message):
    await message.answer(db.get_houre(tg_id=message.from_user.id))