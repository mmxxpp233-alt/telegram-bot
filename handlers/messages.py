from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


async def coming_soon(call: CallbackQuery, title: str):
    await call.answer()

    await call.message.answer(
        f"""🚧 {title}

❌ هذه الميزة غير مفعلة حالياً.

⏳ سيتم إضافتها قريباً."""
    )


# ======================
# QR
# ======================

@router.callback_query(F.data == "qr_create")
async def qr_create(call: CallbackQuery):
    await coming_soon(call, "📱 إنشاء QR")


@router.callback_query(F.data == "qr_read")
async def qr_read(call: CallbackQuery):
    await coming_soon(call, "📷 قراءة QR")


# ======================
# Links
# ======================

@router.callback_query(F.data == "short_link")
async def short_link(call: CallbackQuery):
    await coming_soon(call, "🔗 اختصار الروابط")


@router.callback_query(F.data == "check_link")
async def check_link(call: CallbackQuery):
    await coming_soon(call, "🛡️ فحص الروابط")

# ======================
# Decoration
# ======================

@router.callback_query(F.data == "decorate")
async def decorate(call: CallbackQuery):
    await coming_soon(call, "✨ زخرفة النص")


# ======================
# Text To Speech
# ======================

@router.callback_query(F.data == "tts")
async def tts(call: CallbackQuery):
    await coming_soon(call, "🔊 تحويل النص إلى صوت")


# ======================
# User Info
# ======================

@router.callback_query(F.data == "user_info")
async def user_info(call: CallbackQuery):
    await coming_soon(call, "👤 معلومات المستخدم")


# ======================
# Username Generator
# ======================

@router.callback_query(F.data == "username")
async def username(call: CallbackQuery):
    await coming_soon(call, "🆔 إنشاء يوزر")

# ======================
# Fake Numbers
# ======================

@router.callback_query(F.data == "fake_numbers")
async def fake_numbers(call: CallbackQuery):
    await coming_soon(call, "📲 أرقام وهمية")


# ======================
# Bot Maker
# ======================

@router.callback_query(F.data == "bot_maker")
async def bot_maker(call: CallbackQuery):
    await coming_soon(call, "🤖 صانع البوتات")


# ======================
# Developer
# ======================

@router.callback_query(F.data == "developer")
async def developer(call: CallbackQuery):
    await coming_soon(call, "👨‍💻 المطور")

# ======================
# Unknown Callbacks
# ======================

@router.callback_query()
async def unknown_callback(call: CallbackQuery):
    await call.answer()

    await call.message.answer(
        "⚠️ هذا الزر غير مبرمج حالياً.\n\n"
        "🚧 سيتم تفعيله في التحديث القادم."
    )
    
