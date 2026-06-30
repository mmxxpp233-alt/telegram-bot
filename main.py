import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.subscription import router as subscription_router

from modules.qr.handler import router as qr_router
from modules.links.handler import router as links_router


async def main():
    bot = Bot(BOT_TOKEN)

    dp = Dispatcher()

    # Handlers
    dp.include_router(start_router)
    dp.include_router(subscription_router)

    # Modules
    dp.include_router(qr_router)
    dp.include_router(links_router)

    print("✅ Bot Started")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
