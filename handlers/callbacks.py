import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from config import START_IMAGE, BOT_NAME
from handlers.subscription import check_subscriptions
from keyboards.menus import main_menu
from states import BotStates

router = Router()


# =========================
# 🔐 الاشتراك الإجباري
# =========================
@router.callback_query(F.data == "check_sub")
async def check_sub(call: CallbackQuery):

    msg = await call.message.answer("⏳ جاري التحقق من الاشتراك...")

    await asyncio.sleep(1)
    await msg.edit_text("🔍 يتم فحص القنوات...")

    ok = await check_subscriptions(call.bot, call.from_user.id)

    if not ok:
        await msg.edit_text("❌ أنت لسه مش مشترك في كل القنوات")
        await call.answer("غير مكتمل", show_alert=True)
        return

    await msg.delete()
    await call.answer("✅ تم التحقق بنجاح")

    user_name = call.from_user.first_name

    await call.message.answer(
        f"🎉 شكراً لاشتراكك في {BOT_NAME}"
    )

    await call.message.answer_photo(
        photo=START_IMAGE,
        caption=f"""
👋 أهلاً بك عزيزي {user_name}

🤖 تم دخولك للقائمة الرئيسية
اختر من الأزرار 👇
""",
        reply_markup=main_menu()
    )


# =========================
# 📱 QR CREATE
# =========================
@router.callback_query(F.data == "qr_create")
async def qr_create(call: CallbackQuery, state: FSMContext):

    await call.answer()

    await state.set_state(BotStates.qr_create)

    await call.message.answer("📱 أرسل النص الذي تريد تحويله إلى QR")


# =========================
# 📷 QR READ
# =========================
@router.callback_query(F.data == "qr_read")
async def qr_read(call: CallbackQuery, state: FSMContext):

    await call.answer()

    await state.set_state(BotStates.qr_read)

    await call.message.answer("📷 أرسل صورة QR التي تريد قراءتها")


# =========================
# 🔗 SHORT LINK
# =========================
@router.callback_query(F.data == "short_link")
async def short_link(call: CallbackQuery, state: FSMContext):

    await call.answer()

    await state.set_state(BotStates.short_link)

    await call.message.answer("🔗 أرسل الرابط الذي تريد اختصاره")


# =========================
# 🛡️ CHECK LINK
# =========================
@router.callback_query(F.data == "check_link")
async def check_link(call: CallbackQuery, state: FSMContext):

    await call.answer()

    await state.set_state(BotStates.check_link)

    await call.message.answer("🛡️ أرسل الرابط الذي تريد فحصه")


# =========================
# ✨ DECORATE
# =========================
@router.callback_query(F.data == "decorate")
async def decorate(call: CallbackQuery, state: FSMContext):

    await call.answer()

    await state.set_state(BotStates.decorate_type)

    await call.message.answer(
        "✨ اختر نوع الزخرفة (عربي / إنجليزي) من خلال الرسالة التالية"
    )


# =========================
# 🔊 TTS
# =========================
@router.callback_query(F.data == "tts")
async def tts(call: CallbackQuery, state: FSMContext):

    await call.answer()

    await state.set_state(BotStates.tts_gender)

    await call.message.answer(
        "🔊 اختر نوع الصوت: (👦 ولد / 👧 بنت)"
    )


# =========================
# 👤 USER INFO
# =========================
@router.callback_query(F.data == "user_info")
async def user_info(call: CallbackQuery):

    await call.answer()

    user = call.from_user

    await call.message.answer_photo(
        photo=user.photo[0].file_id if user.photo else START_IMAGE,
        caption=f"""
👤 معلومات المستخدم:

🆔 ID: {user.id}
👤 الاسم: {user.full_name}
📛 اليوزر: @{user.username if user.username else 'لا يوجد'}
"""
    )


# =========================
# 🆔 USERNAME
# =========================
@router.callback_query(F.data == "username")
async def username(call: CallbackQuery, state: FSMContext):

    await call.answer()

    await state.set_state(BotStates.username_type)

    await call.message.answer(
        "🆔 اختر نوع اليوزر:\n\n"
        "1 - عشوائي\n"
        "2 - مميز\n"
        "3 - نوع خاص"
    )


# =========================
# ❓ UNKNOWN
# =========================
@router.callback_query()
async def unknown(call: CallbackQuery):

    await call.answer()

    await call.message.answer(
        "⚠️ هذا الزر غير مبرمج حالياً"
    )
