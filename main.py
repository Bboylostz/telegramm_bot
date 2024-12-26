import asyncio
import logging
import sys
from aiogram import Bot
from config import BOT_TOKEN
from hendlers import dp


logging.basicConfig(level=logging.INFO, stream=sys.stdout)

async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("бот выключен")
