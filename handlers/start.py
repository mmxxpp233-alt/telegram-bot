from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from handlers.subscription import check_subscriptions
from keyboards.menus import main_menu
from config import START_IMAGE

router = Router()


def subscribe_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="𝗰𝗵𝗮𝗻𝗻𝗲𝗹❶", url="https://t.me/feraon_1")],
        [InlineKeyboardButton(text="𝗰𝗵𝗮𝗻𝗻𝗲𝗹❷", url="https://t.me/my_botg1")],
        [InlineKeyboardButton(text="𝗰𝗵𝗮𝗻𝗻𝗲𝗹❸", url="https://t.me/fraon10k")],
        [InlineKeyboardButton(text="✅ تحقق", callback_data="check_sub")]
    ])


@router.callback_query(F.data == "check_sub")
async def check_sub(call):

    ok = await check_subscriptions(call.bot, call.from_user.id)

    if not ok:
        await call.answer("❌ لسه مش مشترك في كل القنوات", show_alert=True)
        return

    await call.answer("✅ تم التحقق بنجاح")

    await call.message.delete()

    user_name = call.from_user.first_name

    await call.message.answer_photo(
        photo=START_IMAGE,
        caption=f"🎉 شكراً لاشتراكك يا {user_name}\nتم دخولك للبوت 🤖",
        reply_markup=main_menu()
    )
