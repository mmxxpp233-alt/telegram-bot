from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from config import BOT_TOKEN

from handlers.start import start_handler
from handlers.check import check_handler
from handlers.menu import menu_handler


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CallbackQueryHandler(check_handler, pattern="check"))
    app.add_handler(CallbackQueryHandler(menu_handler))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
