import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(intents = discord.Intents.all(), command_prefix='[')

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

bot.run('MTA1Nzg2ODYzNjExNjc1NDQ3Mw.GIsBMZ.EJr3O3kWJev1DiOwYaBngyf_mM4k7BiPjbYZv4')
