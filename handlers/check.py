from telegram.ext import ContextTypes
from utils.channels import is_joined
from handlers.menu import show_menu
from config import SUCCESS_MESSAGE

async def check_handler(update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    if await is_joined(user_id, context.bot):
        await query.message.delete()
        await query.message.chat.send_message(SUCCESS_MESSAGE)
        await show_menu(query.message)
    else:
        await query.answer("❌ لازم تشترك في كل القنوات", show_alert=True)
