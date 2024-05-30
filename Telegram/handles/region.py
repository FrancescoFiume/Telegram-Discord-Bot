
from telegram import Update,  Chat
from telegram.ext import  CallbackContext
from Model.Model import Chat, db, Region

async def chinese(update: Update, context: CallbackContext):

    chat = update.effective_chat
    message = update.effective_message
    if db.is_closed():
        db.connect()

    admins_id = []
    user = ""
    try:
        admins = await context.bot.get_chat_administrators(chat.id)
        admins_id = [admin.user.id for admin in admins]

    except Exception as e:
        user = Chat.get(chat_id=chat.id)
    if message.from_user.id in admins_id or user.is_private_chat:

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

    db.connect()
    admins_id = []
    user = ""
    try:
        admins = await context.bot.get_chat_administrators(chat.id)
        admins_id = [admin.user.id for admin in admins]

    except Exception as e:
        user = Chat.get(chat_id=chat.id)
    if message.from_user.id in admins_id or user.is_private_chat:
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

