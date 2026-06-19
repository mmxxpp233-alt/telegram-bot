from config import CHANNELS

async def is_joined(user_id, bot):
    for ch in CHANNELS:
        member = await bot.get_chat_member(ch, user_id)
        if member.status in ["left", "kicked"]:
            return False
    return True
