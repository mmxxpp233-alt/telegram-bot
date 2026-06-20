import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart

from config import BOT_TOKEN, START_IMAGE

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# القنوات
CHANNELS = ["@feraon_1", "@my_botg1", "@fraon10k"]

# ---------------- CHECK SUB ----------------
async def is_subscribed(user_id: int):
    for ch in CHANNELS:
        try:
            member = await bot.get_chat_member(ch, user_id)
            if member.status in ["left", "kicked"]:
                return False
        except:
            return False
    return True


# ---------------- MAIN MENU ----------------
def main_menu():
    return types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="📱 رقم جديد", callback_data="new_number")]
    ])


# ---------------- START ----------------
@dp.message(CommandStart())
async def start(message: types.Message):

    ok = await is_subscribed(message.from_user.id)

    if not ok:
        kb = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="📢 قناة 1", url="https://t.me/feraon_1")],
            [types.InlineKeyboardButton(text="📢 قناة 2", url="https://t.me/my_botg1")],
            [types.InlineKeyboardButton(text="📢 قناة 3", url="https://t.me/fraon10k")],
            [types.InlineKeyboardButton(text="🔄 تحقق", callback_data="check")]
        ])

        await message.answer_photo(
            photo=START_IMAGE,
            caption="❌ لازم تشترك في القنوات أولاً",
            reply_markup=kb
        )
        return

    await message.answer_photo(
        photo=START_IMAGE,
        caption="🎉 تم التحقق بنجاح\nمرحباً بك",
        reply_markup=main_menu()
    )


# ---------------- CHECK BUTTON ----------------
@dp.callback_query(F.data == "check")
async def check(call: types.CallbackQuery):

    ok = await is_subscribed(call.from_user.id)

    if ok:
        await call.message.edit_caption(
            caption="🎉 تم التحقق بنجاح\nأهلاً بيك",
            reply_markup=main_menu()
        )
    else:
        await call.answer("❌ اشترك في القنوات أولاً", show_alert=True)


# ---------------- NEW NUMBER ----------------
@dp.callback_query(F.data == "new_number")
async def new_number(call: types.CallbackQuery):

    kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="1", callback_data="1"),
            types.InlineKeyboardButton(text="2", callback_data="2"),
            types.InlineKeyboardButton(text="3", callback_data="3"),
            types.InlineKeyboardButton(text="4", callback_data="4"),
        ]
    ])

    await call.message.answer("📞 ابعت رقم الهاتف الآن")
    await call.message.answer("📊 اختر نوع العملية:", reply_markup=kb)


# ---------------- HANDLE NUMBER ----------------
user_numbers = {}

@dp.message(F.text)
async def handle_text(message: types.Message):
    text = message.text

    if text.startswith("+") or text.isdigit():
        user_numbers[message.from_user.id] = text

        await message.delete()

        await message.answer("⏳ جاري المعالجة...")

        await asyncio.sleep(1)

        await message.answer(
            f"""
📱 الرقم: {text}
🌍 تم المعالجة
✅ العملية ناجحة
"""
        )


# ---------------- RUN ----------------
async def main():
    print("Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
