from aiogram import Router, F

router = Router()


@router.callback_query(F.data == "tts")
async def tts(call):
    await call.answer()
    await call.message.answer("🔊 أرسل النص لتحويله لصوت")


@router.callback_query(F.data == "decorate")
async def decorate(call):
    await call.answer()
    await call.message.answer("✨ أرسل النص للزخرفة")


@router.callback_query(F.data == "check_link")
async def check_link(call):
    await call.answer()
    await call.message.answer("🔗 أرسل الرابط للفحص")


@router.callback_query(F.data == "qr_create")
async def qr_create(call):
    await call.answer()
    await call.message.answer("📷 أرسل النص لإنشاء QR")


@router.callback_query(F.data == "qr_read")
async def qr_read(call):
    await call.answer()
    await call.message.answer("📷 أرسل صورة QR لقراءتها")


@router.callback_query(F.data == "short_link")
async def short_link(call):
    await call.answer()
    await call.message.answer("🌐 أرسل الرابط لاختصاره")


@router.callback_query(F.data == "user_gen")
async def user_gen(call):
    await call.answer()
    await call.message.answer("👤 إنشاء يوزر سيتم لاحقًا")


@router.callback_query(F.data == "bot_create")
async def bot_create(call):
    await call.answer()
    await call.message.answer("🤖 إنشاء بوت سيتم لاحقًا")


@router.callback_query(F.data == "dev")
async def dev(call):
    await call.answer()
    await call.message.answer("👨‍💻 تواصل مع المطور")


@router.callback_query(F.data == "ip_protect")
async def ip(call):
    await call.answer()
    await call.message.answer("🛡 حماية IP سيتم تطويرها لاحقًا")
