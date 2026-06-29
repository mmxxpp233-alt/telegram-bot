import asyncio

from aiogram import Router, F
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from config import (
    CHANNELS,
    BOT_NAME,
    START_IMAGE,
)

from keyboards.main_menu import main_menu

router = Router()


def subscription_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✨ القناة الأولى",
                    url=f"https://t.me/{CHANNELS[0].replace('@', '')}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ القناة الثانية",
                    url=f"https://t.me/{CHANNELS[1].replace('@', '')}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ القناة الثالثة",
                    url=f"https://t.me/{CHANNELS[2].replace('@', '')}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✅ تحقق",
                    callback_data="check_sub"
                )
            ]
        ]
    )


async def check_subscriptions(bot, user_id: int):
    for channel in CHANNELS:
        try:
            member = await bot.get_chat_member(channel, user_id)

            if member.status in ("left", "kicked"):
                return False

        except Exception:
            return False

    return True


@router.callback_query(F.data == "check_sub")
async def check_sub(call: CallbackQuery):

    msg = await call.message.answer(
        "⏳ جاري التحقق من الاشتراك..."
    )

    await asyncio.sleep(1)

    await msg.edit_text(
        "🔍 يتم فحص القنوات..."
    )

    ok = await check_subscriptions(
        call.bot,
        call.from_user.id,
    )

if not ok:
        await msg.edit_text(
            "❌ أنت لست مشتركًا في جميع القنوات."
        )

        await call.answer(
            "اشترك أولاً ثم أعد المحاولة",
            show_alert=True,
        )

        return

    await msg.delete()

    await call.answer(
        "✅ تم التحقق بنجاح"
    )

    await call.message.answer(
        f"🎉 شكراً لاشتراكك في {BOT_NAME}"
    )

    await call.message.answer_photo(
        photo=START_IMAGE,
        caption=f"""
👋 أهلاً بك {call.from_user.first_name}

🤖 تم التحقق من اشتراكك بنجاح.

اختر الخدمة التي تريدها من القائمة بالأسفل 👇
""",
        reply_markup=main_menu(),
    )
