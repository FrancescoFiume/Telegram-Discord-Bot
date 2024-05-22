
from telegram import Update,  Chat
from telegram.ext import  CallbackContext
from Model.Model import db, Tweeter

async def show(update: Update, context: CallbackContext):
    if db.is_closed():
        db.connect()
    tweeters = Tweeter.select()
    global_tweeters = []
    chinese = []
    for tweeter in tweeters:
        if tweeter.code_id == "GL":
            print(tweeter.tweeter_name)
            global_tweeters.append(tweeter.tweeter_name)
        else:
            chinese.append(tweeter.tweeter_name)
    global_tweeters = "\n".join(global_tweeters)
    chinese = "\n".join(chinese)




    db.close()
    await update.message.reply_text("Gloabl Tweeters:\n"+ global_tweeters +
                                    "\nChinese Tweeteers\n:" + chinese)
