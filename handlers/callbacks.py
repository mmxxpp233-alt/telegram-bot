import asyncio
from aiogram import Router, F
from aiogram.types import Message

from config import START_IMAGE, BOT_NAME, ADMIN_IDS
from handlers.subscription import check_subscriptions
from keyboards.menus import main_menu

router = Router()


@router.callback_query(F.data == "check_sub")
async def check_sub(call):

    # ⏳ Loading وهمي احترافي
    msg = await call.message.answer("⏳ جاري التحقق من الاشتراك...")

    await asyncio.sleep(1)
    await msg.edit_text("🔍 يتم فحص القنوات...")

    await asyncio.sleep(1)
    await msg.edit_text("📡 التحقق من البيانات...")

    ok = await check_subscriptions(call.bot, call.from_user.id)

    # ❌ غير مشترك
    if not ok:
        await msg.edit_text("❌ انت لسه مش مشترك في قنوات المطور")
        await call.answer("غير مكتمل", show_alert=True)
        return

    await msg.delete()
    await call.answer("✅ تم التحقق بنجاح")

    user_name = call.from_user.first_name
    user_id = call.from_user.id

    # 🟡 إشعار للأدمن عند دخول أي مستخدم
    try:
        for admin in ADMIN_IDS:
            await call.bot.send_message(
                admin,
                f"📥 مستخدم دخل البوت\n\n👤 الاسم: {user_name}\n🆔 ID: {user_id}"
            )
    except:
        pass

    # 🎉 رسالة النجاح
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
