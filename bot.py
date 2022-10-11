# This example requires the 'message_content' intent.

from http import client
import discord, os, weather, uonet, mysql_c
from vulcan import Keystore, Account, Vulcan
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

intent = discord.Intents.default()
intent.members = True
intent.message_content = True

bot = commands.Bot(command_prefix='$', intents=intent);

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
    
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
@bot.command()
async def plan(ctx, date=""):
    await ctx.send(embed = await uonet.GetTimetableEmbed(VClient, date)) 
@bot.command()
async def oceny(ctx):
    await ctx.send(embed = await uonet.GetGradesEmbed(VClient))
@bot.command()
async def pogoda(ctx):
    await ctx.send(embed = weather.GetWeatherEmbed())
@bot.command()
async def numerek(ctx, date=""):
    await ctx.send(embed = await uonet.GetLuckyNumberEmbed(VClient, date))
@bot.command()
async def sprawdziany(ctx):
    await ctx.send(embed = await uonet.GetExamsEmbed(VClient))
@bot.command()
async def zadania(ctx):
    await ctx.send(embed = await uonet.GetHomeworkEmbed(VClient))
    await ctx.send(embed = mysql_c.readHomework())
@bot.command()
async def dodajzadanie(ctx, x, y, z, w):
    mysql_c.addHomework(x, y, z, w)
    await ctx.send("Pomyślnie dodano zadanie :)")
async def dodajtest(ctx, x, y, z, w):
    mysql_c.addExam(x, y, z, w)
    await ctx.send("Pomyślnie dodano test :)")

bot.run(os.getenv("DISCORD_TOKEN"))



