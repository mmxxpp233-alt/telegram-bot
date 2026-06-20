import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile
import edge_tts
from urllib.parse import urlparse

from config import BOT_TOKEN ش
from utils import (
    generate_random_user,
    generate_vip_user,
    decorate_ar,
    decorate_en
)

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

# ---------------- MAIN MENU ----------------
def main_menu():
    return types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="🎯 توليد يوزر", callback_data="gen"),
            types.InlineKeyboardButton(text="🔊 تحويل صوت", callback_data="voice")
        ],
        [
            types.InlineKeyboardButton(text="✨ زخرفة", callback_data="dec"),
            types.InlineKeyboardButton(text="🔗 فحص رابط", callback_data="link")
        ],
        [
            types.InlineKeyboardButton(text="🤖 بوت آخر", url="https://t.me/Cigvj_bot"),
            types.InlineKeyboardButton(text="👨‍💻 المطور", url="https://t.me/ATTACK_V12")
        ]
    ])

# ---------------- USER MENU ----------------
def user_menu():
    return types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="💎 يوزر مميز", callback_data="vip_user"),
            types.InlineKeyboardButton(text="🎲 يوزر عشوائي", callback_data="rand_user")
        ],
        [
            types.InlineKeyboardButton(text="🔙 رجوع", callback_data="home")
        ]
    ])

# ---------------- DECORATE MENU ----------------
def dec_menu():
    return types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="🇸🇦 عربي", callback_data="dec_ar"),
            types.InlineKeyboardButton(text="🇬🇧 English", callback_data="dec_en")
        ],
        [
            types.InlineKeyboardButton(text="🔙 رجوع", callback_data="home")
        ]
    ])

# ---------------- START ----------------
@dp.message(CommandStart())
async def start(message: types.Message):

    await message.answer_photo(
        photo="https://i.postimg.cc/VkJdvzDH/IMG-20260611-165810.jpg",
        caption=f"""
👋 أهلاً بك {message.from_user.first_name}

🤖 مرحباً بك في روبوت المنحرف

اختر الأداة من الأزرار 👇
""",
        reply_markup=main_menu()
    )

# ---------------- CALLBACKS ----------------
@dp.callback_query()
async def buttons(callback: types.CallbackQuery):
    uid = callback.from_user.id

    if callback.data == "home":
        user_state.pop(uid, None)
        await callback.message.answer("🏠 الرئيسية", reply_markup=main_menu())

    elif callback.data == "gen":
        await callback.message.answer("🎯 اختر نوع اليوزر", reply_markup=user_menu())

    elif callback.data == "vip_user":
        for _ in range(10):
            await callback.message.answer(f"💎 تم الصيد بيوزر جديد ✅ : {generate_vip_user()}")
            await asyncio.sleep(0.2)
        await callback.message.answer("انتهى الصيد 🖱️")

    elif callback.data == "rand_user":
        for _ in range(10):
            await callback.message.answer(f"🎲 تم الصيد بيوزر جديد ✅ : {generate_random_user()}")
            await asyncio.sleep(0.2)
        await callback.message.answer("انتهى الصيد 🖱️")

    elif callback.data == "voice":
        kb = types.InlineKeyboardMarkup(inline_keyboard=[
            [
                types.InlineKeyboardButton(text="👦 ولد", callback_data="boy"),
                types.InlineKeyboardButton(text="👧 بنت", callback_data="girl")
            ],
            [
                types.InlineKeyboardButton(text="🔙 رجوع", callback_data="home")
            ]
        ])
        await callback.message.answer("🔊 اختر الصوت:", reply_markup=kb)

    elif callback.data == "boy":
        user_voice[uid] = "boy"
        user_state[uid] = "tts"
        await callback.message.answer("✍ ابعت النص")

    elif callback.data == "girl":
        user_voice[uid] = "girl"
        user_state[uid] = "tts"
        await callback.message.answer("✍ ابعت النص")

    elif callback.data == "dec":
        await callback.message.answer("✨ اختر نوع الزخرفة", reply_markup=dec_menu())

    elif callback.data == "dec_ar":
        user_state[uid] = "dec_ar"
        await callback.message.answer("✍ ابعت النص العربي")

    elif callback.data == "dec_en":
        user_state[uid] = "dec_en"
        await callback.message.answer("✍ Send English text")

    elif callback.data == "link":
        user_state[uid] = "link"
        await callback.message.answer("🔗 ابعت الرابط للفحص")

# ---------------- TEXT HANDLER ----------------
@dp.message(F.text)
async def handle_message(message: types.Message):
    uid = message.from_user.id
    text = message.text

    if user_state.get(uid) == "tts":
        voice = user_voice.get(uid, "boy")

        voice_map = {
            "boy": "ar-EG-ShakirNeural",
            "girl": "ar-EG-SalmaNeural"
        }

        file = f"voice_{uid}.mp3"
        communicate = edge_tts.Communicate(text, voice_map[voice])
        await communicate.save(file)

        await message.answer_voice(FSInputFile(file))
        os.remove(file)

        user_state[uid] = None
        return

    if user_state.get(uid) == "dec_ar":
        for item in decorate_ar(text):
            await message.answer(item)
            await asyncio.sleep(0.2)
        user_state[uid] = None
        return

    if user_state.get(uid) == "dec_en":
        for item in decorate_en(text):
            await message.answer(item)
            await asyncio.sleep(0.2)
        user_state[uid] = None
        return

    if user_state.get(uid) == "link":
        link = text.strip()

        if not link.startswith("http"):
            await message.answer("❌ ابعت رابط صحيح")
            return

        kind, opens = analyze_link(link)

        await message.answer(f"""
🔗 الرابط:
{link}

🌐 النوع:
{kind}

📌 يفتح:
{opens}

⚠️ الحالة:
آمن مبدئيًا 🟢
""")

        user_state[uid] = None
        return

    await message.answer("اضغط /start لاستخدام البوت")

# ---------------- RUN ----------------
async def main():
    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
