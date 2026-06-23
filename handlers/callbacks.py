from aiogram import Router, F
import asyncio

from handlers.subscription import check_subscriptions
from keyboards.menus import main_menu, subscribe_keyboard
from config import START_IMAGE, BOT_NAME

router = Router()


@router.callback_query(F.data == "check_sub")
async def check_sub(call):

    # ⏳ رسالة تحميل وهمي
    msg = await call.message.answer("⏳ جاري التحقق من الاشتراك...")

    await asyncio.sleep(1)
    await msg.edit_text("🔍 يتم فحص القنوات...")

    ok = await check_subscriptions(call.bot, call.from_user.id)

    # ❌ غير مشترك
    if not ok:
        await msg.edit_text("❌ أنت لسه مش مشترك في كل القنوات")
        await call.answer("غير مكتمل", show_alert=True)
        return

    # 🟢 مشترك فعلاً
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

🤖 تم دخولك إلى القائمة الرئيسية
اختر من الأزرار 👇
""",
        reply_markup=main_menu()
    )
