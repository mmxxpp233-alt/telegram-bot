from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# زرار واحد فقط
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="تشغيل البوت 🚀")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("أهلاً 👋", reply_markup=keyboard)

@dp.message()
async def handle(message: types.Message):
    if message.text == "تشغيل البوت 🚀":
        await message.answer("البوت شغال ✅")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
