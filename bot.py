import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='[',intents= intents )


@bot.event

async def on_ready():
    print(">>Bot is online <<")

bot.run('MTA1Nzg2ODYzNjExNjc1NDQ3Mw.Gdv9AX.ALP4R8uSkWBRIg6EvXpXxi_vr45AthVDaXYuSE')
