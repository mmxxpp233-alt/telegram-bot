from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.menus import main_menu
from config import START_IMAGE
from handlers.subscription import check_subscriptions

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

    user_name = message.from_user.first_name

    ok = await check_subscriptions(message.bot, message.from_user.id)

    if not ok:
        await message.answer_photo(
            photo=START_IMAGE,
            caption=f"⚠️ لازم تشترك أولاً يا {user_name} 🛡️",
            reply_markup=subscribe_keyboard()
        )
        return

    await message.answer_photo(
        photo=START_IMAGE,
        caption=f"👋 أهلاً بك يا {user_name}\n\nتم دخولك بنجاح 🤖",
        reply_markup=main_menu()
    )
