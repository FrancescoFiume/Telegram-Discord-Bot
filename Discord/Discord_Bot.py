#!/usr/bin/python3
import os
import sys

import rpyc



sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Api.Discord_Api import discord_api

from Discord.Message_Polishing import Polisher
import discord
from discord.ext import commands
import re

from multiprocessing import Queue

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    pass
    print(f"Bot is ready. Logged in as {bot.user.name} ({bot.user.id})")


def get_channel_and_message_ids(url):
    pattern = r'https?://discord\.com/channels/(\d+)/(\d+)/?'
    match = re.match(pattern, url)
    if match:
        channel_id = int(match.group(1))
        message_id = int(match.group(2))
        return channel_id, message_id
    else:
        raise ValueError("Invalid Discord message URL")



@bot.event
async def on_message(message):
    allowed_channel_ids = [1112874435326771300, 1112877289844264960]
    if message.author == bot.user:
        return
    if message.channel.id not in allowed_channel_ids:
        return

    #Polishing Message Content
    message.content = Polisher(message.content)
    print(message.content)


    forwarding = {
        "region" : message.content[0:2],
        "message": message.content
    }
    telegram_conn = rpyc.connect("localhost", 18812)
    telegram_conn.root.send_message(forwarding)
    await bot.process_commands(message)


def run_discord_on_daemon():
    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix="!", intents=intents)

    bot.run(discord_api)


if __name__ == '__main__':

    bot.run(discord_api)
