from config import CHANNELS, SUCCESS_MESSAGE
from handlers.menu import show_menu
from utils.channels import is_joined

async def check_handler(update, context):
    query = update.callback_query
    user_id = query.from_user.id

    if await is_joined(user_id, context.bot, CHANNELS):
        await query.message.delete()
        await query.message.chat.send_message(SUCCESS_MESSAGE)
        await show_menu(query.message)
    else:
        await query.answer("❌ لازم تشترك في كل القنوات", show_alert=True)
