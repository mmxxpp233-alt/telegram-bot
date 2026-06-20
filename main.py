import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile, InputMediaPhoto
import edge_tts
from urllib.parse import urlparse

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

user_state = {}
user_voice = {}

# ---------------- LINK ANALYZER ----------------
def analyze_link(link: str):
    domain = urlparse(link).netloc.lower()

    if "wa.me" in domain or "whatsapp" in domain:
        return "واتساب", "جروب واتساب"
    elif "t.me" in domain:
        return "تيليجرام", "قناة / بوت تيليجرام"
    elif "tiktok.com" in domain:
        return "تيك توك", "فيديوهات تيك توك"
    elif "instagram.com" in domain:
        return "انستجرام", "بروفايل / منشورات"
    elif "facebook.com" in domain:
        return "فيسبوك", "منشورات / صفحة"
    else:
        return "موقع عام", "موقع إلكتروني"

# ---------------- MENUS ----------------
def main_menu():
    return types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="🎯 توليد يوزر", callback_data="gen"),
            types.InlineKeyboardButton(text="🔊 تحويل صوت", callback_data="voice")
        ],
        [
            types.InlineKeyboardButton(text="✨ زخرفة", callback_data="dec"),
            types.InlineKeyboardButton(text="🔗 فحص رابط", callback_data="link")
        ]
    ])


def back_btn():
    return types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="🔙 رجوع", callback_data="home")]
    ])


def user_menu():
    return types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="💎 يوزر مميز", callback_data="vip_user"),
            types.InlineKeyboardButton(text="🎲 يوزر عشوائي", callback_data="rand_user")
        ],
        [types.InlineKeyboardButton(text="🔙 رجوع", callback_data="home")]
    ])


def voice_menu():
    return types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="👦 ولد", callback_data="boy"),
            types.InlineKeyboardButton(text="👧 بنت", callback_data="girl")
        ],
        [types.InlineKeyboardButton(text="🔙 رجوع", callback_data="home")]
    ])


def dec_menu():
    return types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="🇸🇦 عربي", callback_data="dec_ar"),
            types.InlineKeyboardButton(text="🇬🇧 English", callback_data="dec_en")
        ],
        [types.InlineKeyboardButton(text="🔙 رجوع", callback_data="home")]
    ])

# ---------------- START ----------------
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer_photo(
        photo="https://i.postimg.cc/VkJdvzDH/IMG-20260611-165810.jpg",
        caption=f"👋 أهلاً {message.from_user.first_name}\n\nاختر من القائمة 👇",
        reply_markup=main_menu()
    )

# ---------------- CALLBACK HANDLER (IMPORTANT) ----------------
@dp.callback_query()
async def cb(call: types.CallbackQuery):
    uid = call.from_user.id

    # HOME
    if call.data == "home":
        user_state.pop(uid, None)
        await call.message.edit_caption(
            caption="🏠 القائمة الرئيسية 👇",
            reply_markup=main_menu()
        )

    # GEN MENU
    elif call.data == "gen":
        await call.message.edit_caption(
            caption="🎯 اختر نوع اليوزر 👇",
            reply_markup=user_menu()
        )

    elif call.data == "vip_user":
        text = ""
        for _ in range(5):
            text += f"💎 {uid} -> VIP USER\n"
        await call.message.answer(text)

    elif call.data == "rand_user":
        text = ""
        for _ in range(5):
            text += f"🎲 {uid} -> RANDOM USER\n"
        await call.message.answer(text)

    # VOICE
    elif call.data == "voice":
        await call.message.edit_caption(
            caption="🔊 اختر الصوت 👇",
            reply_markup=voice_menu()
        )

    elif call.data == "boy":
        user_voice[uid] = "boy"
        user_state[uid] = "tts"
        await call.message.answer("✍ ابعت النص")

    elif call.data == "girl":
        user_voice[uid] = "girl"
        user_state[uid] = "tts"
        await call.message.answer("✍ ابعت النص")

    # DECORATION
    elif call.data == "dec":
        await call.message.edit_caption(
            caption="✨ اختر الزخرفة 👇",
            reply_markup=dec_menu()
        )

    elif call.data == "dec_ar":
        user_state[uid] = "dec_ar"
        await call.message.answer("✍ ابعت النص العربي")

    elif call.data == "dec_en":
        user_state[uid] = "dec_en"
        await call.message.answer("✍ Send English text")

    # LINK
    elif call.data == "link":
        user_state[uid] = "link"
        await call.message.answer("🔗 ابعت الرابط")

    await call.answer()

# ---------------- TEXT HANDLER ----------------
@dp.message(F.text)
async def text_handler(message: types.Message):
    uid = message.from_user.id
    text = message.text

    # LINK MODE
    if user_state.get(uid) == "link":
        kind, opens = analyze_link(text)
        await message.answer(f"🔗 النوع: {kind}\n📌 يفتح: {opens}")
        user_state[uid] = None
        return

    await message.answer("اضغط /start")

# ---------------- RUN ----------------
async def main():
    print("Bot running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
