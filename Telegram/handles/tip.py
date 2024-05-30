from telegram import Update
from telegram.ext import CallbackContext


async def tip(update: Update, context: CallbackContext):

    message = update.effective_message
    await message.reply_text("You can't tip me directly, but you can tip @Ffrrn1")
