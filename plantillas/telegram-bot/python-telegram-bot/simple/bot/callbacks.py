from telegram import Update
from telegram.ext import ContextTypes

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="¡Has presionado el botón!")
