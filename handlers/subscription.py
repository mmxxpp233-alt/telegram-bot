from config import CHANNELS


async def check_subscriptions(bot, user_id: int):

    for channel in CHANNELS:
        try:
            member = await bot.get_chat_member(channel, user_id)

            if member.status in ["left", "kicked"]:
                return False

        except Exception:
            return False

    return True
