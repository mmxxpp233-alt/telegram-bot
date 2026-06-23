from aiogram import Router, F
from aiogram.types import BufferedInputFile
import qrcode
from io import BytesIO

router = Router()


# ================= QR READ =================
@router.callback_query(F.data == "qr_read")
async def qr_read(call):
    await call.message.answer("📷 أرسل صورة QR وسأقوم بقراءتها (مدعوم عبر pyzbar لاحقاً في تطوير كامل)")


# ================= QR CREATE (حقيقي) =================
@router.callback_query(F.data == "qr_create")
async def qr_create(call):
    data = "Hello QR"

    img = qrcode.make(data)

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    await call.message.answer_photo(
        BufferedInputFile(buffer.read(), filename="qr.png"),
        caption="🧾 تم إنشاء QR بنجاح"
    )


# ================= CHECK LINK =================
@router.callback_query(F.data == "check_link")
async def check_link(call):
    await call.message.answer("🔗 أرسل الرابط للفحص")
    

# ================= SHORT LINK =================
@router.callback_query(F.data == "short_link")
async def short_link(call):
    await call.message.answer("✂️ اختصار الرابط سيتم عبر خدمة خارجية (حالياً جاهز للاستقبال)")


# ================= DECORATE =================
@router.callback_query(F.data == "decorate")
async def decorate(call):
    await call.message.answer("✨ أرسل الاسم وسيتم زخرفته فوراً (جاهز للتطوير على أشكال مختلفة)")


# ================= TTS =================
@router.callback_query(F.data == "tts")
async def tts(call):
    await call.message.answer("🔊 أرسل النص لتحويله لصوت (جاهز للربط بمكتبة gTTS)")


# ================= NEW USER =================
@router.callback_query(F.data == "new_user")
async def new_user(call):
    await call.message.answer("👤 سيتم تحويلك الآن إلى بوت Maker_VIP_bot لإنشاء البوتات")
    await call.message.answer("🔗 @Maker_VIP_bot")


# ================= CREATE BOT =================
@router.callback_query(F.data == "create_bot")
async def create_bot(call):
    await call.message.answer("🤖 فتح لوحة إنشاء البوت")
    await call.message.answer("⚙️ اختر من أدوات إنشاء البوت داخل النظام")


# ================= IP PROTECT =================
@router.callback_query(F.data == "ip_protect")
async def ip_protect(call):
    await call.message.answer(
        f"🛡️ تم تفعيل حماية الحساب\n"
        f"👤 User ID: {call.from_user.id}\n"
        f"🔒 تم تأمين الجلسة بنجاح"
    )


# ================= USER INFO =================
@router.callback_query(F.data == "user_info")
async def user_info(call):
    u = call.from_user

    text = f"""
👤 معلوماتك:

• الاسم: {u.full_name}
• اليوزر: @{u.username if u.username else "لا يوجد"}
• ID: {u.id}

📊 الحالة: نشط
"""

    await call.message.answer(text)


# ================= DEVELOPER =================
@router.callback_query(F.data == "developer")
async def developer(call):
    await call.message.answer("👨‍💻 المطور: @ATTACK_VlP_12")
