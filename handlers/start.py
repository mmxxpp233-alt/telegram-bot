from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.menus import main_menu
from config import START_IMAGE
from handlers.subscription import check_subscriptions

router = Router()


@router.message(CommandStart())
async def start_cmd(message):

    ok = await check_subscriptions(message.bot, message.from_user.id)

    if not ok:

        kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="𓏺 قناة ❶",
                        url="https://t.me/feraon_1"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="𓏺 قناة ❷",
                        url="https://t.me/my_botg1"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="𓏺 قناة ❸",
                        url="https://t.me/fraon10k"
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

        await message.answer_photo(
            photo=START_IMAGE,
            caption="لازم تشترك في قنوات المطور أولاً 🛡️",
            reply_markup=kb
        )
        return

    await message.answer_photo(
        photo=START_IMAGE,
        caption="👋 أهلاً بك في البوت",
        reply_markup=main_menu()
    )
