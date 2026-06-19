async def is_joined(user_id, bot, channels):
    for ch in channels:
        member = await bot.get_chat_member(ch, user_id)
        if member.status in ["left", "kicked"]:
            return False
    return True
