from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import START_IMAGE, SUB_IMAGE, BOT_NAME
from handlers.subscription import check_subscriptions
from keyboards.menus import main_menu

router = Router()


def subscribe_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="𝗰𝗵𝗮𝗻𝗻𝗲𝗹❶", url="https://t.me/feraon_1")],
        [InlineKeyboardButton(text="𝗰𝗵𝗮𝗻𝗻𝗲𝗹❷", url="https://t.me/my_botg1")],
        [InlineKeyboardButton(text="𝗰𝗵𝗮𝗻𝗻𝗲𝗹❸", url="https://t.me/fraon10k")],
        [InlineKeyboardButton(text="✅ تحقق", callback_data="check_sub")]
    ])


@router.message(CommandStart())
async def start_cmd(message):

    ok = await check_subscriptions(message.bot, message.from_user.id)

    # ❌ غير مشترك
    if not ok:
        await message.answer_photo(
            photo=SUB_IMAGE,
            caption=f"""
👋 أهلاً بك يا {message.from_user.first_name}

⚠️ يجب الاشتراك في القنوات أولاً
ثم اضغط "تحقق" 👇
""",
            reply_markup=subscribe_keyboard()
        )
        return

    # 🟢 مشترك
    await message.answer_photo(
        photo=START_IMAGE,
        caption=f"""
👋 أهلاً بك عزيزي {message.from_user.first_name}
🤖 {BOT_NAME}

اختر من القائمة 👇
""",
        reply_markup=main_menu()
    )
