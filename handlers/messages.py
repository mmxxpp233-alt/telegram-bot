from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, BufferedInputFile
import qrcode
from io import BytesIO
from gtts import gTTS
import requests
from pyzbar.pyzbar import decode
from PIL import Image

router = Router()

# ================= STATE بسيط =================
user_state = {}  # تخزين حالة المستخدم


# ================= BACK =================
@router.callback_query(F.data == "back")
async def back(call: CallbackQuery):
    user_state.pop(call.from_user.id, None)
    await call.message.answer("🔙 رجعت للقائمة الرئيسية")
    await call.answer()


# ================= QR CREATE =================
@router.callback_query(F.data == "qr_create")
async def qr_create(call: CallbackQuery):
    user_state[call.from_user.id] = "qr"
    await call.message.answer("🧾 أرسل النص لتحويله إلى QR")
    await call.answer()


# ================= QR READ =================
@router.callback_query(F.data == "qr_read")
async def qr_read(call: CallbackQuery):
    user_state[call.from_user.id] = "qr_read"
    await call.message.answer("📷 أرسل صورة QR")
    await call.answer()


# ================= TTS =================
@router.callback_query(F.data == "tts")
async def tts(call: CallbackQuery):
    user_state[call.from_user.id] = "tts"
    await call.message.answer("🔊 أرسل النص لتحويله لصوت")
    await call.answer()


# ================= CHECK LINK =================
@router.callback_query(F.data == "check_link")
async def check_link(call: CallbackQuery):
    user_state[call.from_user.id] = "check_link"
    await call.message.answer("🔗 أرسل الرابط لفحصه")
    await call.answer()


# ================= SHORT LINK (TinyURL) =================
@router.message()
async def handle_all(message: Message):

    uid = message.from_user.id
    state = user_state.get(uid)

    text = message.text

    # ============ QR CREATE ============
    if state == "qr" and text:
        img = qrcode.make(text)
        bio = BytesIO()
        img.save(bio, format="PNG")
        bio.seek(0)

        await message.answer_photo(
            BufferedInputFile(bio.read(), filename="qr.png"),
            caption="📷 تم إنشاء QR بنجاح"
        )
        return

    # ============ TTS ============
    if state == "tts" and text:
        tts = gTTS(text=text, lang="ar")
        bio = BytesIO()
        tts.write_to_fp(bio)
        bio.seek(0)

        await message.answer_voice(
            BufferedInputFile(bio.read(), filename="voice.mp3"),
            caption="🔊 تم التحويل لصوت"
        )
        return

    # ============ CHECK LINK ============
    if state == "check_link" and text:
        try:
            r = requests.get(text, timeout=5)
            await message.answer(
                f"🔍 الرابط يعمل\n📊 Status: {r.status_code}"
            )
        except:
            await message.answer("❌ الرابط غير صالح أو لا يمكن الوصول له")
        return

    # ============ QR READ ============
    if state == "qr_read" and message.photo:
        file = await message.bot.get_file(message.photo[-1].file_id)
        img_bytes = await message.bot.download_file(file.file_path)

        img = Image.open(img_bytes)
        result = decode(img)

        if result:
            data = result[0].data.decode()
            await message.answer(f"📷 النص داخل QR:\n\n{data}")
        else:
            await message.answer("❌ لم أستطع قراءة QR")
        return

    # fallback
    await message.answer("⚠️ اختر وظيفة من القائمة أولاً")
