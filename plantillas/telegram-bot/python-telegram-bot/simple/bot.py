from telegram.ext import Application
from bot.handlers import setup_handlers
from config import BOT_TOKEN

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    setup_handlers(app)

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
