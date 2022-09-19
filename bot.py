# This example requires the 'message_content' intent.

import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="panią E."))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

bot.run(os.getenv("DISCORD_TOKEN"))
