# This example requires the 'message_content' intent.

from http import client
import discord, os, weather, uonet, asyncio
from vulcan import Keystore, Account, Vulcan
from dotenv import load_dotenv


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

with open("keystore.json") as f:
    keystore = Keystore.load(f)
with open("account.json") as f:
    account = Account.load(f)



@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="panią E."))
    global VClient
    VClient = Vulcan(keystore, account)
    await VClient.select_student()
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('$pogoda'):
        await message.channel.send(embed=weather.GetWeatherEmbed())

    if message.content.startswith('$plan'):
        await message.channel.send(embed = await uonet.GetTimetableEmbed(VClient)) 

    if message.content.startswith('$numerek'):
        await message.channel.send(embed = await uonet.GetLuckyNumberEmbed(VClient))
    
    if message.content.startswith('$oceny'):
        await message.channel.send(embed = await uonet.GetGradesEmbed(VClient))

        
bot.run(os.getenv("DISCORD_TOKEN"))
