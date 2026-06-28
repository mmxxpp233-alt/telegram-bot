from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states import BotStates
from services.qr import create_qr, read_qr

router = Router()


# =========================
# 📱 QR CREATE
# =========================
@router.message(BotStates.qr_create)
async def qr_create_handler(message: Message, state: FSMContext):

    text = message.text

    if not text:
        await message.answer("❌ من فضلك أرسل نص فقط")
        return

    await message.answer("⏳ جاري إنشاء QR...")

    path = create_qr(text)

    await message.answer_photo(
        photo=path,
        caption="✅ تم إنشاء QR بنجاح"
    )

    await state.clear()


# =========================
# 📷 QR READ
# =========================
@router.message(BotStates.qr_read)
async def qr_read_handler(message: Message, state: FSMContext):

    if not message.photo:
        await message.answer("❌ من فضلك أرسل صورة QR فقط")
        return

    file = await message.bot.get_file(message.photo[-1].file_id)
    downloaded = await message.bot.download_file(file.file_path)

    temp_path = "qr_temp.png"

    with open(temp_path, "wb") as f:
        f.write(downloaded.read())

    result = read_qr(temp_path)

    if not result:
        await message.answer("❌ لم يتم العثور على QR")
    else:
        await message.answer(f"📄 النص داخل QR:\n\n{result}")

    await state.clear()

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states import BotStates

router = Router()


# =========================
# 🔗 SHORT LINK
# =========================
@router.message(BotStates.short_link)
async def handle_short_link(message: Message, state: FSMContext):

    url = message.text

    if not url or not url.startswith("http"):
        await message.answer("❌ أرسل رابط صحيح يبدأ بـ http")
        return

    await message.answer("⏳ جاري اختصار الرابط...")

    # 🔥 هنا مؤقتًا (Placeholder)
    short_url = f"https://short.ly/{url[-6:]}"

    await message.answer(
        f"🔗 تم اختصار الرابط بنجاح:\n\n{short_url}"
    )

    await state.clear()


# =========================
# 🛡️ CHECK LINK
# =========================
@router.message(BotStates.check_link)
async def handle_check_link(message: Message, state: FSMContext):

    url = message.text

    if not url or not url.startswith("http"):
        await message.answer("❌ أرسل رابط صحيح")
        return

    await message.answer("🛡️ جاري فحص الرابط...")

    # 🔥 تحليل بسيط
    domain = url.split("//")[-1].split("/")[0]

    result = f"""
🛡️ نتيجة فحص الرابط:

🔗 الرابط: {url}
🌐 الدومين: {domain}
📊 الحالة: آمن مبدئيًا
"""

    await message.answer(result)

    await state.clear()

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states import BotStates
from config import MALE_VOICE, FEMALE_VOICE
from gtts import gTTS
import uuid

router = Router()


# =========================
# ✨ DECORATION (ARABIC / ENGLISH)
# =========================
@router.message(BotStates.decorate_text)
async def handle_decorate(message: Message, state: FSMContext):

    text = message.text

    if not text:
        await message.answer("❌ أرسل نص فقط")
        return

    await message.answer("✨ جاري زخرفة النص...")

    # زخرفة بسيطة (تقدر تطورها لاحقًا)
    decorated = f"✨『 {text} 』✨\n★ {text} ★\n✧ {text} ✧"

    await message.answer(decorated)

    await state.clear()


# =========================
# 🔊 TEXT TO SPEECH (TTS)
# =========================
@router.message(BotStates.tts_text)
async def handle_tts(message: Message, state: FSMContext):

    text = message.text

    if not text:
        await message.answer("❌ أرسل نص فقط")
        return

    await message.answer("🔊 جاري تحويل النص لصوت...")

    # 🔥 توليد صوت
    file_name = f"voice_{uuid.uuid4().hex}.mp3"

    tts = gTTS(text=text, lang="ar")
    tts.save(file_name)

    await message.answer_voice(voice=open(file_name, "rb"))

    await state.clear()

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import random
import string

from states import BotStates
from config import USERNAME_COUNT, USERNAME_MIN, USERNAME_MAX, START_IMAGE

router = Router()

# =========================
# 👤 USER INFO
# =========================
@router.message(BotStates.waiting_input)
async def user_info_handler(message: Message):

    user = message.from_user

    text = f"""
👤 معلومات المستخدم:

🆔 ID: {user.id}
👤 الاسم: {user.full_name}
📛 اليوزر: @{user.username if user.username else 'لا يوجد'}
"""

    await message.answer_photo(
        photo=START_IMAGE,
        caption=text
    )


# =========================
# 🆔 USERNAME GENERATOR
# =========================
@router.message(BotStates.username_type)
async def username_handler(message: Message, state: FSMContext):

    choice = message.text

    usernames = []

    # =========================
    # 🔹 RANDOM USERNAMES
    # =========================
    if choice == "1":

        for _ in range(USERNAME_COUNT):
            length = random.randint(USERNAME_MIN, USERNAME_MAX)
            name = ''.join(random.choices(string.ascii_lowercase, k=length))
            usernames.append(f"@{name}")

        result = "🆔 يوزرات عشوائية:\n\n" + "\n".join(usernames)


    # =========================
    # 🔹 PREMIUM USERNAMES (SIMULATED)
    # =========================
    elif choice == "2":

        base = ["pro", "vip", "king", "official", "team"]

        for b in base:
            usernames.append(f"@{b}_{random.randint(10,999)}")

        result = "✨ يوزرات مميزة:\n\n" + "\n".join(usernames)


    # =========================
    # 🔹 SHORT USERNAMES
    # =========================
    else:

        for _ in range(10):
            name = ''.join(random.choices(string.ascii_lowercase, k=3))
            usernames.append(f"@{name}{random.randint(1,99)}")

        result = "⚡ يوزرات قصيرة:\n\n" + "\n".join(usernames)

    await message.answer(result)
    await state.clear()
    
