
from telegram import Update,  Chat
from telegram.ext import  CallbackContext
from Model.Model import Chat, db

async def new_chat_member(update: Update, context: CallbackContext):

    chat = update.effective_chat
    message = update.effective_message
    admins = await context.bot.get_chat_administrators(chat.id)
    admins_id = [admin.user.id for admin in admins]
    if message.from_user.id in admins_id:
        db.connect()
        try:
          chat_obj = Chat.get(chat_id = str(update.effective_chat.id))
          if chat_obj:
              await update.message.reply_text("Chat has been added to the forwarder already. Choose the region you want to forward from")
              return
        except Exception as e:
            if chat.title == None:
                Chat.create(chat_id=chat.id, chat_name=chat.username, is_forum=False, is_private_chat=True)

            elif chat.is_forum:
                Chat.create(chat_id=chat.id, chat_name=chat.title, is_forum=True, is_private_chat=False)
                await update.message.reply_text(
                    "Send '/here' command to select the thread you want me to post in, otherwise I'll be posting in the main thread")

            else:
                Chat.create(chat_id=chat.id, chat_name=chat.title, is_forum=False, is_private_chat=False)




        finally:
            await update.message.reply_text(
                "send '/global' command to add tweets from the global community\nsend /chinese to add tweets from the chinese community")
            db.close()


    else:
        await update.message.reply_text("You are not an admin")


