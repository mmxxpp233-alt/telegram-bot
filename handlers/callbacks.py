from aiogram import Router, F

router = Router()


@router.callback_query(F.data == "new_number")
async def new_number(call):
    await call.answer()
    await call.message.answer("📱 ميزة رقم جديد سيتم تطويرها قريبًا")


@router.callback_query(F.data == "tts")
async def tts(call):
    await call.answer()
    await call.message.answer("🔊 أرسل النص لتحويله لصوت")


@router.callback_query(F.data == "decorate")
async def decorate(call):
    await call.answer()
    await call.message.answer("✨ أرسل النص للزخرفة")


# 🔗 فحص رابط
@router.callback_query(F.data == "check_link")
async def check_link(call):
    await call.answer()
    await call.message.answer("🔗 أرسل الرابط للفحص")


# 📊 معلومات
@router.callback_query(F.data == "info")
async def info(call):
    await call.answer()
    await call.message.answer("📊 هذا بوت احترافي قيد التطوير")


# ⚙️ إعدادات
@router.callback_query(F.data == "settings")
async def settings(call):
    await call.answer()
    await call.message.answer("⚙️ الإعدادات سيتم تطويرها لاحقًا")
