import qrcode
from io import BytesIO

from aiogram import Router, F
from aiogram.types import (
    Message,
    CallbackQuery,
    BufferedInputFile,
)
from aiogram.fsm.context import FSMContext

from handlers.states import BotStates

router = Router()

# ==========================
# إنشاء QR
# ==========================

@router.callback_query(F.data == "qr_create")
async def qr_create(call: CallbackQuery, state: FSMContext):

    await state.set_state(BotStates.qr_create)

    await call.message.answer(
        "📱 أرسل النص الذي تريد تحويله إلى QR."
    )

    await call.answer()


@router.message(BotStates.qr_create)
async def qr_create_process(message: Message, state: FSMContext):

    if not message.text:

        await message.answer(
            "❌ مسموح بإرسال نص فقط."
        )

        return

    img = qrcode.make(message.text)

    bio = BytesIO()

    img.save(bio, "PNG")

    bio.seek(0)

    await message.answer_photo(
        BufferedInputFile(
            bio.read(),
            filename="qr.png"
        ),
        caption="✅ تم إنشاء رمز QR بنجاح."
    )

    await state.clear()
    import aiohttp

# ==========================
# قراءة QR
# ==========================

@router.callback_query(F.data == "qr_read")
async def qr_read(call: CallbackQuery, state: FSMContext):

    await state.set_state(BotStates.qr_read)

    await call.message.answer(
        "📷 أرسل صورة الـ QR لفك الشفرة."
    )

    await call.answer()


@router.message(BotStates.qr_read)
async def qr_read_process(message: Message, state: FSMContext):

    if not message.photo:

        await message.answer(
            "❌ أرسل صورة QR فقط."
        )

        return

    await message.answer(
        "⚠️ سيتم تفعيل قراءة QR في الجزء الأخير من المشروع."
    )

    await state.clear()


# ==========================
# اختصار الروابط
# ==========================

@router.callback_query(F.data == "short_link")
async def short_link(call: CallbackQuery, state: FSMContext):

    await state.set_state(BotStates.short_link)

    await call.message.answer(
        "🔗 أرسل الرابط الذي تريد اختصاره."
    )

    await call.answer()


@router.message(BotStates.short_link)
async def short_link_process(message: Message, state: FSMContext):

    if not message.text:

        await message.answer("❌ أرسل رابطاً صحيحاً.")

        return

    async with aiohttp.ClientSession() as session:

        async with session.get(
            f"https://tinyurl.com/api-create.php?url={message.text}"
        ) as response:

            short_url = await response.text()

    await message.answer(
        f"✅ الرابط المختصر:\n\n{short_url}"
    )

    await state.clear()
    # ==========================
# فحص الروابط
# ==========================

@router.callback_query(F.data == "check_link")
async def check_link(call: CallbackQuery, state: FSMContext):

    await state.set_state(BotStates.link_check)

    await call.message.answer(
        "🛡️ أرسل الرابط المراد فحصه."
    )

    await call.answer()


@router.message(BotStates.link_check)
async def check_link_process(message: Message, state: FSMContext):

    if not message.text:

        await message.answer("❌ أرسل رابطاً صحيحاً.")

        return

    url = message.text.lower()

    site = "غير معروف"

    if "facebook" in url:
        site = "Facebook"

    elif "instagram" in url:
        site = "Instagram"

    elif "tiktok" in url:
        site = "TikTok"

    elif "telegram" in url or "t.me" in url:
        site = "Telegram"

    elif "youtube" in url:
        site = "YouTube"

    await message.answer(
        f"""🛡️ نتيجة الفحص

🌐 الرابط:
{message.text}

📌 النوع:
{site}
"""
    )

    await state.clear()


# ==========================
# زخرفة النص
# ==========================

@router.callback_query(F.data == "decorate")
async def decorate(call: CallbackQuery, state: FSMContext):

    await state.set_state(BotStates.decorate)

    await call.message.answer(
        "✨ أرسل النص الذي تريد زخرفته."
    )

    await call.answer()


@router.message(BotStates.decorate)
async def decorate_process(message: Message, state: FSMContext):

    text = message.text

    await message.answer(
        f"""✨ تم إنشاء الزخرفة

{text}
『{text}』
★{text}★
꧁{text}꧂
✦{text}✦
"""
    )

    await state.clear()
    
