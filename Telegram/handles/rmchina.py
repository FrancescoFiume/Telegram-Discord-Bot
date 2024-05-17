
from telegram import Update,  Chat
from telegram.ext import  CallbackContext
from Model.Model import Chat, db, Region

async def rmchina(update: Update, context: CallbackContext):

    chat = update.effective_chat
    message = update.effective_message
    admins = await context.bot.get_chat_administrators(chat.id)
    admins_id = [admin.user.id for admin in admins]
    if message.from_user.id in admins_id:
        db.connect()
        try:
            region_obj = Region.get(chat_id=chat.id, code="CN")
            region_obj.delete_instance()
            await update.message.reply_text("Region removed successfully")
        except Exception:
            await update.message.reply_text("Region not found in this chat")
        finally:
            db.close()

    else:
        await update.message.reply_text("You are not an admin")

