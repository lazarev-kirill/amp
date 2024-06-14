from config import BOT_TOKEN, ADMIN_ID
from handlers import router

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.methods import SendMessage
import asyncio
import logging

from test_module import test_module


async def on_start():
    return SendMessage("Bot is up and running", chat_id=ADMIN_ID)


async def on_stop():
    return SendMessage("Bot is stop", chat_id=ADMIN_ID)


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    test_module("test")
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
