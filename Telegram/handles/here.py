
from telegram import Update,  Chat, Message
from telegram.ext import  CallbackContext
from Model.Model import Chat, db, Region

async def here(update: Update, context: CallbackContext):

    chat = update.effective_chat
    message = update.effective_message
    admins = await context.bot.get_chat_administrators(chat.id)
    admins_id = [admin.user.id for admin in admins]
    if chat.is_forum:

        if message.from_user.id in admins_id:
            db.connect()
            try:
                chat_model = Chat.get(chat_id=chat.id)
                thread_id = message.message_thread_id
                if not chat_model.topic_id == thread_id:

                    print(chat_model.chat_id+" in DB")
                    print(chat.id)

                    chat_model.topic_id = str(thread_id)
                    chat_model.save()
                    await update.message.reply_text(f"Messages will be forwarded in this thread")
                else:
                    await update.message.reply_text(f"Current thread is selected already")

            except Exception as e:
                print(e)
                await update.message.reply_text("You need to send /forward first")
            finally:
                db.close()
        else:
            await update.message.reply_text("You are not an admin")


    else:

        await update.message.reply_text("This chat is not a forum chat")


