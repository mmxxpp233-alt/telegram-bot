import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.subscription import router as subscription_router


async def main():
    bot = Bot(BOT_TOKEN)

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(subscription_router)

    print("✅ Bot Started")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
