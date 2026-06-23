import qrcode
import aiohttp
from io import BytesIO
from gtts import gTTS

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, BufferedInputFile
from aiogram.fsm.context import FSMContext

from handlers.states import BotStates

router = Router()


# ================= BACK =================
@router.callback_query(F.data == "back")
async def back(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer("🔙 رجوع للقائمة الرئيسية")
    await call.answer()


# ================= QR CREATE =================
@router.callback_query(F.data == "qr_create")
async def qr_create(call: CallbackQuery, state: FSMContext):
    await state.set_state(BotStates.qr_create)
    await call.message.answer("📷 ابعت النص لتحويله QR")


@router.message(BotStates.qr_create)
async def qr_create_text(message: Message, state: FSMContext):
    img = qrcode.make(message.text)

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    await message.answer_photo(
        BufferedInputFile(buffer.read(), filename="qr.png"),
        caption="🧾 تم إنشاء QR"
    )

    await state.clear()


# ================= QR READ =================
@router.callback_query(F.data == "qr_read")
async def qr_read(call: CallbackQuery, state: FSMContext):
    await state.set_state(BotStates.qr_read)
    await call.message.answer("📷 ابعت صورة QR")

@router.message(BotStates.qr_read)
async def qr_read_img(message: Message, state: FSMContext):
    await message.answer("❌ الخدمة غير متاحة حالياً بسبب الضغط على السيرفر")
    await state.clear()


# ================= LINK CHECK =================
@router.callback_query(F.data == "check_link")
async def check_link(call: CallbackQuery, state: FSMContext):
    await state.set_state(BotStates.link_check)
    await call.message.answer("🔗 ابعت الرابط للفحص")


@router.message(BotStates.link_check)
async def check_link_process(message: Message, state: FSMContext):

    url = message.text

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as r:
                status = r.status
        except:
            await message.answer("❌ الرابط غير صالح")
            await state.clear()
            return

    await message.answer(
        f"""🔍 نتيجة الفحص:

🌐 الرابط: {url}
📊 الحالة: {status}
"""
    )

    await state.clear()


# ================= SHORT LINK =================
@router.callback_query(F.data == "short_link")
async def short_link(call: CallbackQuery, state: FSMContext):
    await state.set_state(BotStates.short_link)
    await call.message.answer("✂️ ابعت الرابط لاختصاره")


@router.message(BotStates.short_link)
async def short_link_process(message: Message, state: FSMContext):

    url = message.text

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://tinyurl.com/api-create.php?url={url}") as r:
            short = await r.text()

    await message.answer(f"🔗 الرابط المختصر:\n{short}")

    await state.clear()


# ================= TTS =================
@router.callback_query(F.data == "tts")
async def tts(call: CallbackQuery, state: FSMContext):
    await state.set_state(BotStates.tts_type)
    await call.message.answer("🎤 اختار النوع: (ولد / بنت)")


@router.message(BotStates.tts_type)
async def tts_type(message: Message, state: FSMContext):

    if message.text not in ["ولد", "بنت"]:
        await message.answer("❌ اختار ولد أو بنت فقط")
        return

    await state.update_data(tts_type=message.text)
    await state.set_state(BotStates.tts_text)

    await message.answer("📝 ابعت النص لتحويله لصوت")


@router.message(BotStates.tts_text)
async def tts_text(message: Message, state: FSMContext):

    data = await state.get_data()
    voice_type = data.get("tts_type")

    tts = gTTS(text=message.text, lang="ar")

    bio = BytesIO()
    tts.write_to_fp(bio)
    bio.seek(0)

    await message.answer_voice(
        BufferedInputFile(bio.read(), filename="voice.mp3"),
        caption=f"🔊 صوت ({voice_type})"
    )

    await state.clear()


# ================= USER INFO =================
@router.callback_query(F.data == "user_info")
async def user_info(call: CallbackQuery):

    u = call.from_user

    await call.message.answer(
        f"""👤 معلوماتك:

• الاسم: {u.full_name}
• اليوزر: @{u.username}
• ID: {u.id}
"""
    )


# ================= CREATE BOT =================
@router.callback_query(F.data == "create_bot")
async def create_bot(call: CallbackQuery):
    await call.message.answer("🤖 افتح: @Maker_VlP_bot")


# ================= IP PROTECT =================
@router.callback_query(F.data == "ip_protect")
async def ip(call: CallbackQuery):
    await call.message.answer("🛡️ تم تفعيل الحماية (تنبيه فقط)")
