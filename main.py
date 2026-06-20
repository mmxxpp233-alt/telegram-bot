import asyncio
from aiogram import Bot, Dispatcher, types, F
from config import BOT_TOKEN
from handlers import main_menu, countries_menu, build_result
from countries import COUNTRIES

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

user_data = {}

@dp.message()
async def start(message: types.Message):
    await message.answer("👋 اختر الخدمة", reply_markup=main_menu())


@dp.callback_query(F.data == "get_number")
async def get_number(call: types.CallbackQuery):
    await call.message.answer("🌍 اختر الدولة:", reply_markup=countries_menu())


@dp.callback_query(F.data.startswith("country_"))
async def country_selected(call: types.CallbackQuery):
    key = call.data.split("_")[1]
    country = COUNTRIES[key]

    text, code = build_result(country)

    # رسالة
    await call.message.answer(text)

    # فويس (مؤقت)
    await call.message.answer("🔊 Voice: code sent")

    # زر نسخ
    kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="📋 نسخ الكود", callback_data=f"copy_{code}")]
    ])

    await call.message.answer("⬇️", reply_markup=kb)


@dp.callback_query(F.data.startswith("copy_"))
async def copy_code(call: types.CallbackQuery):
    code = call.data.split("_")[1]
    await call.answer(f"تم نسخ الكود: {code}", show_alert=True)


async def main():
    print("Bot running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
