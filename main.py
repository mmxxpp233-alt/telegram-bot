import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

# 📌 استيراد الروترات
from handlers import start, callbacks, messages
from bot_commands import set_commands   # ⭐ أضفنا أوامر الثلاث نقاط


async def main():

    # 🤖 إنشاء البوت
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # 📌 ربط الملفات (Routers)
    dp.include_router(start.router)
    dp.include_router(callbacks.router)
    dp.include_router(messages.router)

    # ⭐ تفعيل أوامر الثلاث نقاط
    await set_commands(bot)

    # 🚀 تشغيل البوت
    print("🚀 Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
