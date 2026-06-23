import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import start, callbacks, messages
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# ربط كل الهاندلرز
dp.include_router(start.router)
dp.include_router(callbacks.router)
dp.include_router(messages.router)

async def main():
    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
