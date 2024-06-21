from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters.command import Command
from handlers import router
import asyncio

from colorama import init
init()
from colorama import Fore, Back, Style

async def main(): 
    bot = Bot(token="")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(Style.BRIGHT+Fore.RED+"BOT TURN OFF")