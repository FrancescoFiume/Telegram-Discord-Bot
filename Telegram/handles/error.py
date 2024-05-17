import logging

from telegram import Update,  Chat
from telegram.ext import CallbackContext, ContextTypes
from Model.Model import Chat, db


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.error(msg="Exception while handling an update:", exc_info=context.error)
    try:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="An error occurred. Please try again later.")
    except Exception as e:
        logging.error(f"Failed to send error message: {e}")