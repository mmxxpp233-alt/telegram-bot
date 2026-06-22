from aiogram import Router, F

from keyboards.menus import main_menu
from handlers.subscription import check_subscriptions
from config import START_IMAGE

router = Router()


@router.callback_query(F.data == "new_number")
async def new_number(call):
    await call.answer()

    await call.message.answer("📱 زر رقم جديد جاهز للتطوير لاحقًا")


@router.callback_query(F.data == "tts")
async def tts(call):
    await call.answer()

    await call.message.answer("🔊 ميزة تحويل النص لصوت سيتم إضافتها لاحقًا")


@router.callback_query(F.data == "decorate")
async def decorate(call):
    await call.answer()

    await call.message.answer("✨ ميزة الزخرفة سيتم إضافتها لاحقًا")


# =========================
# 🔥 زر التحقق من الاشتراك
# =========================
@router.callback_query(F.data == "check_sub")
async def check_sub(call):

    ok = await check_subscriptions(call.bot, call.from_user.id)

    if not ok:
        await call.answer("❌ لازم تشترك في القنوات أولاً", show_alert=True)
        return

    await call.message.delete()

    await call.message.answer_photo(
        photo=START_IMAGE,
        caption="🎉 تم التحقق بنجاح\nأهلاً بيك",
        reply_markup=main_menu()
    )

    await call.answer()
