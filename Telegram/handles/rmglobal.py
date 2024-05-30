from telegram import Update, Chat
from telegram.ext import CallbackContext
from Model.Model import Chat, db, Region


async def rmglobal(update: Update, context: CallbackContext):

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
            region_obj = Region.get(chat_id=chat.id, code="GL")
            region_obj.delete_instance()
            if chat.is_forum:
                await update.message.reply_text("Region removed successfully")
        except Exception:
            await update.message.reply_text("Region not found in this chat")
        finally:
            db.close()
    else:
        await update.message.reply_text("You are not an admin")

