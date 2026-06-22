import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import callbacks, messages

BOT_TOKEN = "PUT_YOUR_TOKEN_HERE"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# ربط الملفات
dp.include_router(callbacks.router)
dp.include_router(messages.router)


async def main():
    print("Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
