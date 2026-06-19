from telegram.ext import ContextTypes
from utils.channels import is_joined
from handlers.menu import menu_keyboard
from config import SUCCESS_MESSAGE, MENU_IMAGE, OWNER_USERNAME


async def check_handler(update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    if await is_joined(user_id, context.bot):

        await query.message.reply_text(SUCCESS_MESSAGE)

        await query.message.reply_photo(
            photo=MENU_IMAGE,
            caption=f"🏠 اللوحة الرئيسية\n👨‍💻 المطور: {OWNER_USERNAME} 🟦",
            reply_markup=menu_keyboard()
        )

    else:
        await query.answer("❌ لازم تشترك في كل القنوات", show_alert=True)
