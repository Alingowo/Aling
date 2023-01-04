import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='[',intents= intents )

@bot.event

async def on_ready():
    print(">>Bot is online <<")

@bot.event

async def on_member_join(member):
    channel = bot.get_channel(1060215095893954691)
    await channel.send(f'{member}join!')

@bot.event 
async def on_member_remove(member):
    channel = bot.get_channel(1060215095893954691)
    await channel.send(f'{member}leave!')

bot.run('MTA1Nzg2ODYzNjExNjc1NDQ3Mw.GoUyhv.TmIbY0NpiD8oRl6d26At7NK8fppfyNSFJQldh0')
