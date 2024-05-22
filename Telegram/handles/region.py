
from telegram import Update,  Chat
from telegram.ext import  CallbackContext
from Model.Model import Chat, db, Region

async def chinese(update: Update, context: CallbackContext):

    chat = update.effective_chat
    message = update.effective_message
    admins = await context.bot.get_chat_administrators(chat.id)
    admins_id = [admin.user.id for admin in admins]
    if message.from_user.id in admins_id:
        db.connect()
        try:
            Region.get(chat_id=str(chat.id), code="CN")
            await update.message.reply_text("Region Connected Already")
        except Exception as e:

            Region.create(code ="CN", chat_id=str(chat.id))
            await update.message.reply_text("Region Connected Successfully")
        finally:
            db.close()

    else:
        await update.message.reply_text("You are not an admin")



async def global_region(update: Update, context: CallbackContext):

    chat = update.effective_chat
    message = update.effective_message
    admins = await context.bot.get_chat_administrators(chat.id)
    admins_id = [admin.user.id for admin in admins]
    if message.from_user.id in admins_id:
        db.connect()
        try:
            Region.get(chat_id=str(chat.id), code="GL")
            await update.message.reply_text("Region Connected Already")
        except Exception as e:

            Region.create(code="GL", chat_id=str(chat.id))
            await update.message.reply_text("Region Connected Successfully")
        finally:
            db.close()

    else:
        await update.message.reply_text("You are not an admin")

