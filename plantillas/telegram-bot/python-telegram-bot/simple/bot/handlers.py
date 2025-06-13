from telegram.ext import CommandHandler, CallbackQueryHandler
from .commands import start, help_command
from .callbacks import button_click

def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button_click))
