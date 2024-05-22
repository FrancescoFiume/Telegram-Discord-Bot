from telegram import Update
from telegram.ext import CallbackContext


async def help(update: Update , context: CallbackContext):
    message = update.effective_message
    await message.reply_text(f"/start - A friendly greeting\n"
                                    f"/forward - Register Chat\n"
                                    f"/global - Ask to receive tweets from global community\n"
                                    f"/chinese - Ask to receive chinese tweets\n"
                                    f"/here - Modify forum thread where you want tweets posted in\n"
                                    "/rmchinese - Remove chinese tweets from forwarding\n"
                                    "/rmglobal - Remove global tweets from forwarding\n"
                                    "/tip - Informations about tipping\n"
                                    "/tweeters - List of all the tweeters\n")
