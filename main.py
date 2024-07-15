from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters.command import Command
import asyncio
import logging
from handlers import router

from colorama import init
init()
from colorama import Fore, Back, Style

from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

async def main():
    bot = Bot(token="6587114212:AAEQDJHhz3dD7SnXiRfAg43qgV_HLOxdKK8")
    dp = Dispatcher()
    logger.info("Starting the bot...")
    dp.include_router(router)
    logger.info("Router included")
    await dp.start_polling(bot)
    logger.info("Polling started")
    await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.warning("Bot stopped by KeyboardInterrupt")
        print(Style.BRIGHT + Fore.RED + "BOT TURN OFF")
    except Exception as e:
        logger.error("An unexpected error occurred", exc_info=True)

