import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

# Handlers
from handlers.start import router as start_router
from handlers.subscription import router as subscription_router


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(subscription_router)


if __name__ == "__main__":
    asyncio.run(main())
