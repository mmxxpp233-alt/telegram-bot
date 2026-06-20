from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters
from config import BOT_TOKEN, START_IMAGE

waiting_users = set()

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚡ BAD", callback_data="bad")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo=START_IMAGE,
        caption="👋 أهلاً بيك في البوت الاحترافي\n\nاضغط BAD للبحث عن معلومات مستخدم",
        reply_markup=reply_markup
    )

# زرار BAD
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "bad":
        waiting_users.add(query.from_user.id)

        await query.message.reply_text("🔎 ابعت يوزر الشخص الآن (مثال: @username)")

# استقبال اليوزر
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    if user_id not in waiting_users:
        return

    waiting_users.remove(user_id)

    username = update.message.text.strip()

    try:
        chat = await context.bot.get_chat(username)

        name = chat.first_name or "N/A"
        bio = getattr(chat, "bio", "N/A")

        # اللغة (قد لا تكون متاحة دايمًا)
        lang = getattr(chat, "language_code", "N/A")

        text = (
            f"👤 الاسم: {name}\n"
            f"🔗 اليوزر: {username}\n"
            f"📌 موجود: نعم\n"
            f"📝 Bio: {bio}\n"
            f"🌐 اللغة: {lang}"
        )

        await update.message.reply_text(text)

        photos = await context.bot.get_user_profile_photos(chat.id)

        if photos.total_count > 0:
            photo = photos.photos[0][-1].file_id
            await context.bot.send_photo(update.effective_chat.id, photo)

    except Exception:
        await update.message.reply_text(
            "❌ الحساب غير موجود أو خاص\n"
            "📌 أو اليوزر خطأ"
        )

# تشغيل
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
