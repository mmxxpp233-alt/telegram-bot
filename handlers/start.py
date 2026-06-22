from aiogram import Router
from aiogram.filters import CommandStart

from keyboards.menus import main_menu
from config import START_IMAGE

router = Router()


@router.message(CommandStart())
async def start_cmd(message):

    if START_IMAGE:
        await message.answer_photo(
            photo=START_IMAGE,
            caption="👋 أهلاً بك في البوت\n\nاختر من القائمة بالأسفل",
            reply_markup=main_menu()
        )
    else:
        await message.answer(
            "👋 أهلاً بك في البوت\n\nاختر من القائمة بالأسفل",
            reply_markup=main_menu()
        )
