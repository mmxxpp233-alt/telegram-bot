import logging
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

from config import BOT_TOKEN
from handlers.start import start_handler
from handlers.check import check_handler
from handlers.menu import menu_handler


# ===== Logging (مهم جدًا على Railway) =====
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


def main():
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN is missing in environment variables")
        return

    try:
        app = ApplicationBuilder().token(BOT_TOKEN).build()

        # ===== HANDLERS =====
        app.add_handler(CommandHandler("start", start_handler))
        app.add_handler(CallbackQueryHandler(check_handler, pattern="check"))
        app.add_handler(CallbackQueryHandler(menu_handler))

        print("✅ Bot is running...")
        app.run_polling()

    except Exception as e:
        print(f"❌ Error starting bot: {e}")


if __name__ == "__main__":
    main()
