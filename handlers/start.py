from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import (
    START_IMAGE,
    SUB_IMAGE,
    BOT_NAME,
)

from handlers.subscription import (
    subscription_keyboard,
    check_subscriptions,
)

from keyboards.main_menu import main_menu

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    ok = await check_subscriptions(
        message.bot,
        message.from_user.id
    )

    if not ok:

        await message.answer_photo(
            photo=SUB_IMAGE,
            caption=f"""
⚠️ لا يمكنك استخدام {BOT_NAME}

يرجى الاشتراك في جميع القنوات أولاً.

بعد الاشتراك اضغط على زر
✅ تحقق
""",
            reply_markup=subscription_keyboard()
        )
        return

    await message.answer_photo(
        photo=START_IMAGE,
        caption=f""
         💝أهلاً بك {message.from_user.first_name}

مرحبًا بك في {BOT_NAME}

اختر الخدمة التي تريدها من القائمة بالأسفل 👇
""",
        reply_markup=main_menu()
    )
