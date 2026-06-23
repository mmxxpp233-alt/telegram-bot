import asyncio
import random
import string
import aiohttp
from io import BytesIO

from aiogram import Router, F
from aiogram.types import BufferedInputFile, CallbackQuery

import qrcode
from gtts import gTTS

router = Router()

# حفظ اليوزرات لمنع التكرار
used_users = set()


# ================= BACK =================
async def back_menu(call: CallbackQuery):
    await call.message.answer("🔙 رجوع للقائمة الرئيسية")
    await call.answer()


# ================= QR CREATE =================
@router.callback_query(F.data == "qr_create")
async def qr_create(call):
    msg = await call.message.answer("⏳ جاري إنشاء QR...")

    img = qrcode.make("QR DATA")

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    await msg.delete()

    await call.message.answer_photo(
        BufferedInputFile(buffer.read(), filename="qr.png"),
        caption="🧾 تم إنشاء QR بنجاح"
    )


# ================= QR READ (basic) =================
@router.callback_query(F.data == "qr_read")
async def qr_read(call):
    await call.message.answer("📷 أرسل صورة QR (ميزة القراءة تحتاج تطوير مكتبة zbar بشكل كامل)")


# ================= TEXT TO SPEECH =================
@router.callback_query(F.data == "tts")
async def tts(call):
    msg = await call.message.answer("🎤 اختر النوع: ولد أو بنت")

    # تخزين بسيط
    call.bot.user_data = {"tts": True}


# استقبال نص TTS
@router.message()
async def handle_text(message):
    data = getattr(message.bot, "user_data", {})

    if data.get("tts"):
        text = message.text

        tts = gTTS(text=text, lang="ar")
        bio = BytesIO()
        tts.write_to_fp(bio)
        bio.seek(0)

        await message.answer_voice(
            BufferedInputFile(bio.read(), filename="voice.mp3"),
            caption="🔊 تم تحويل النص لصوت"
        )

        message.bot.user_data = {}


# ================= CHECK LINK =================
@router.callback_query(F.data == "check_link")
async def check_link(call):
    await call.message.answer("🔗 أرسل الرابط للفحص")


@router.message()
async def link_checker(message):
    text = message.text

    if text.startswith("http"):
        async with aiohttp.ClientSession() as session:
            async with session.get(text) as r:
                status = r.status

        await message.answer(
            f"""🔍 نتيجة الفحص:

🌐 الرابط: {text}
📊 الحالة: {status}
"""
        )


# ================= SHORT LINK =================
@router.callback_query(F.data == "short_link")
async def short_link(call):
    await call.message.answer("✂️ أرسل الرابط لاختصاره")


@router.message()
async def shorten(message):
    if message.text.startswith("http"):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://tinyurl.com/api-create.php?url={message.text}") as r:
                short = await r.text()

        await message.answer(f"🔗 الرابط المختصر:\n{short}")


# ================= USER INFO =================
@router.callback_query(F.data == "user_info")
async def user_info(call):
    u = call.from_user

    photo = await call.bot.get_user_profile_photos(u.id)

    text = f"""
👤 معلومات المستخدم:

• الاسم: {u.full_name}
• اليوزر: @{u.username}
• ID: {u.id}
"""

    await call.message.answer(text)


# ================= CREATE USER (REAL GENERATOR) =================
@router.callback_query(F.data == "new_user")
async def new_user(call):

    chars = string.ascii_letters

    users = []

    while len(users) < 10:
        u = "@" + "".join(random.choice(chars) for _ in range(4))

        if u not in used_users:
            used_users.add(u)
            users.append(u)

    text = "👤 Generated Users:\n\n" + "\n".join(users)

    await call.message.answer(text)


# ================= CREATE BOT =================
@router.callback_query(F.data == "create_bot")
async def create_bot(call):
    await call.message.answer("🤖 افتح هذا البوت:\n@Maker_VlP_bot")


# ================= IP PROTECT =================
@router.callback_query(F.data == "ip_protect")
async def ip(call):
    await call.message.answer("🛡️ تم تفعيل حماية على حسابك (محاكاة آمنة)")


# ================= DEVELOPER =================
@router.callback_query(F.data == "developer")
async def dev(call):
    await call.message.answer("👨‍💻 المطور: @ATTACK_VlP_12")


# ================= BACK BUTTON =================
@router.callback_query(F.data == "back")
async def back(call):
    await back_menu(call)
