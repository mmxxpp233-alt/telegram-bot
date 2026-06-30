from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from modules.links.state import LinkState
from modules.links.service import shorten_url

router = Router()


@router.callback_query(F.data == "short_link")
async def short_link(call: CallbackQuery, state: FSMContext):

    await state.set_state(LinkState.waiting_for_link)

    await call.message.answer(
        "🔗 أرسل الرابط الذي تريد اختصاره."
    )

    await call.answer()

@router.message(LinkState.waiting_for_link)
async def receive_link(message: Message, state: FSMContext):

    url = message.text.strip()

    short = shorten_url(url)

    if not short:
        await message.answer(
            "❌ حدث خطأ أثناء اختصار الرابط."
        )

        await state.clear()
        return

    await message.answer(
        f"✅ الرابط المختصر:\n\n{short}"
    )

    await state.clear()
