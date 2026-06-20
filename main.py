from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "🚫 لا يمكنك الدخول إلى البوت الآن\n\n"
        "💳 هذه الخدمة مدفوعة\n"
        "💰 السعر: 30 دولار\n\n"
        "📞 للتفعيل تواصل مع الدعم"
    )

async def main():
    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
