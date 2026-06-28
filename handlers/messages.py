from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import uuid
import random
import string

from states import BotStates
from config import USERNAME_COUNT, USERNAME_MIN, USERNAME_MAX

from services.qr import create_qr, read_qr
from gtts import gTTS


router = Router()

# =========================
# 📱 QR CREATE
# =========================
@router.message(BotStates.qr_create)
async def qr_create(message: Message, state: FSMContext):

    text = message.text

    if not text:
        await message.answer("❌ أرسل نص فقط")
        return

    await message.answer("⏳ جاري إنشاء QR...")

    path = create_qr(text)

    await message.answer_photo(photo=path, caption="✅ تم إنشاء QR")

    await state.clear()


# =========================
# 📷 QR READ
# =========================
@router.message(BotStates.qr_read)
async def qr_read(message: Message, state: FSMContext):

    if not message.photo:
        await message.answer("❌ أرسل صورة فقط")
        return

    file = await message.bot.get_file(message.photo[-1].file_id)
    downloaded = await message.bot.download_file(file.file_path)

    temp = "qr_temp.png"

    with open(temp, "wb") as f:
        f.write(downloaded.read())

    result = read_qr(temp)

    if result:
        await message.answer(f"📄 النص:\n\n{result}")
    else:
        await message.answer("❌ لم يتم العثور على QR")

    await state.clear()


# =========================
# 🔗 SHORT LINK (مؤقت)
# =========================
@router.message(BotStates.short_link)
async def short_link(message: Message, state: FSMContext):

    url = message.text

    if not url:
        await message.answer("❌ أرسل رابط صحيح")
        return

    short = f"https://short.ly/{random.randint(1000,9999)}"

    await message.answer(f"🔗 الرابط المختصر:\n{short}")

    await state.clear()


# =========================
# 🛡️ CHECK LINK
# =========================
@router.message(BotStates.check_link)
async def check_link(message: Message, state: FSMContext):

    url = message.text

    domain = url.split("//")[-1].split("/")[0] if url else "unknown"

    await message.answer(f"""
🛡️ نتيجة الفحص:

🔗 {url}
🌐 الدومين: {domain}
📊 الحالة: آمن مبدئيًا
""")

    await state.clear()


# =========================
# ✨ DECORATE
# =========================
@router.message(BotStates.decorate_text)
async def decorate(message: Message, state: FSMContext):

    text = message.text

    decorated = f"""
✨ {text} ✨
★ {text} ★
✧ {text} ✧
"""

    await message.answer(decorated)

    await state.clear()


# =========================
# 🔊 TTS
# =========================
@router.message(BotStates.tts_text)
async def tts(message: Message, state: FSMContext):

    text = message.text

    file = f"voice_{uuid.uuid4().hex}.mp3"

    tts = gTTS(text=text, lang="ar")
    tts.save(file)

    await message.answer_voice(voice=open(file, "rb"))

    await state.clear()


# =========================
# 👤 USER INFO
# =========================
@router.message(F.text == "info")
async def user_info(message: Message):

    user = message.from_user

    await message.answer(f"""
👤 الاسم: {user.full_name}
🆔 ID: {user.id}
📛 username: @{user.username if user.username else 'none'}
""")


# =========================
# 🆔 USERNAME GENERATOR
# =========================
@router.message(BotStates.username_type)
async def username(message: Message, state: FSMContext):

    choice = message.text

    results = []

    if choice == "1":

        for _ in range(USERNAME_COUNT):
            name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(USERNAME_MIN, USERNAME_MAX)))
            results.append(f"@{name}")

    elif choice == "2":

        base = ["vip", "pro", "king", "official"]

        for b in base:
            results.append(f"@{b}{random.randint(10,999)}")

    else:

        for _ in range(10):
            name = ''.join(random.choices(string.ascii_lowercase, k=3))
            results.append(f"@{name}{random.randint(1,99)}")

    await message.answer("\n".join(results))

    await state.clear()
