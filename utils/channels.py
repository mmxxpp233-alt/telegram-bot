from config import CHANNELS
from telegram.error import TelegramError


async def is_joined(user_id, bot):
    try:
        for ch in CHANNELS:
            member = await bot.get_chat_member(chat_id=ch, user_id=user_id)

            if member.status in ["left", "kicked"]:
                return False

        return True

    except TelegramError:
        return False
