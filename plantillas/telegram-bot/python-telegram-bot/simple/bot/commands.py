from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Haz clic aquí", callback_data="button_pressed")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("¡Hola! Soy tu bot. Elige una opción:", reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Estos son los comandos disponibles:\n/start - Inicia el bot\n/help - Muestra este mensaje de ayuda")
