import asyncio
import os
import sys
import threading
import rpyc
from rpyc import ThreadedServer
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Api.Telegram_Api import key
import logging
from telegram import Update, ChatMemberUpdated, Message, Chat
from telegram.ext import Updater, CallbackContext, ChatMemberHandler, CommandHandler, ApplicationBuilder, \
    MessageHandler, filters, ContextTypes, TypeHandler, Application

from Model.Model import Region, db
from Telegram.handles.forward import new_chat_member
from Telegram.handles.region import chinese, global_region
from Telegram.handles.here import here
from Telegram.handles.rmchina import rmchina
from Telegram.handles.rmglobal import rmglobal
from Telegram.handles.tip import tip
from Telegram.handles.help import help
from Telegram.handles.show_tweeters import show


base_dir = os.path.dirname((os.path.abspath(__file__)))
bot_path = os.path.join(base_dir, 'Telegram', 'Telegram_Bot.py')


class TelegramService(rpyc.Service):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def exposed_send_message(self, message):
        global application
        future = asyncio.run_coroutine_threadsafe(forward_from_server(message), application.loop)
        try:
            result = future.result(timeout=10)  # Adjust timeout as necessary
        except Exception as e:
            logging.error(f"Unhandled exception in forward_from_server: {e}")













async def forward_from_server(message):
    global application
    try:
        print(message['message'])
        region = message["region"]
        # select chats for that region
        chats_for_region = Region.select().where(Region.code == region)
        '''
        for chat in chats_for_region:
            if chat.chat_id.is_forum:
                if chat.chat_id.topic_id:
                    await application.bot.send_message(chat_id=chat.chat_id.chat_id, text=message['message'][2:],
                                                             message_thread_id=chat.chat_id.topic_id)
                else:
                    await application.bot.send_message(chat_id=chat.chat_id.chat_id, text=message['message'][2:])
            else:
                await application.bot.send_message(chat_id=chat.chat_id.chat_id, text=message['message'][2:])

    except Exception as e:
        logging.error(f"Error in forward_from_server: {e}")
        '''
        for chat in chats_for_region:
            try:
                if chat.chat_id.is_forum:
                    if chat.chat_id.topic_id:
                        await application.bot.send_message(chat_id=chat.chat_id.chat_id, text=message['message'][2:],
                                                           message_thread_id=chat.chat_id.topic_id)
                    else:
                        await application.bot.send_message(chat_id=chat.chat_id.chat_id, text=message['message'][2:])
                else:
                    await application.bot.send_message(chat_id=chat.chat_id.chat_id, text=message['message'][2:])
            except Exception as e:
                logging.error(f"Failed to send message to chat {chat.chat_id.chat_id} with thread {chat.chat_id.topic_id}: {e}")
    except Exception as e:
        logging.error(f"Error in forward_from_server: {e}")

    db.close()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello From Kaspa News Bot.")


def handler_adding(application):
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('forward', new_chat_member))
    application.add_handler(CommandHandler('chinese', chinese))
    application.add_handler(CommandHandler('global', global_region))
    application.add_handler(CommandHandler('here', here))
    application.add_handler(CommandHandler('rmchinese', rmchina))
    application.add_handler(CommandHandler('rmglobal', rmglobal))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(CommandHandler('tipme', tip))
    application.add_handler(CommandHandler('tweeters', show))


def main() -> None:
    application = ApplicationBuilder().token(key).build()
    handler_adding(application)
    application.run_polling()


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    application = ApplicationBuilder().token(key).build()

    handler_adding(application)

    server = ThreadedServer(TelegramService, port=18812)

    server_thread = threading.Thread(target=server.start)

    server_thread.daemon = True
    server_thread.start()
    application.loop = loop
    application.run_polling()

