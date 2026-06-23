import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

# 📌 استيراد الروترات (الملفات الأساسية)
from handlers import start, callbacks, messages


async def main():

    # 🤖 إنشاء البوت
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # 📌 ربط الملفات (Routers)
    dp.include_router(start.router)
    dp.include_router(callbacks.router)
    dp.include_router(messages.router)

    # 🚀 تشغيل البوت
    print("🚀 Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
