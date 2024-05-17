
import subprocess
import os
import threading
import time

def run_telegram_bot():
    base_dir = os.path.dirname((os.path.abspath(__file__)))
    bot_path = os.path.join(base_dir, '../Telegram', 'Telegram_Bot.py')
    process = subprocess.Popen(['python', bot_path])
    process.wait()
def run_discord_bot():
    base_dir = os.path.dirname((os.path.abspath(__file__)))
    bot_path = os.path.join(base_dir, '../Discord', 'Discord_Bot.py')
    process = subprocess.Popen(['python', bot_path])
    process.wait()




telegram_thread = threading.Thread(target=run_telegram_bot)
discord_thread = threading.Thread(target=run_discord_bot)

telegram_thread.start()
discord_thread.start()

# Main script can perform other tasks here if necessary
try:
    while telegram_thread.is_alive() and discord_thread.is_alive():
        time.sleep(1)
except KeyboardInterrupt:
    pass

telegram_thread.join()
discord_thread.join()