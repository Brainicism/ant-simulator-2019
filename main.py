import discord
import configparser
from discord.ext import commands
config = configparser.ConfigParser()
config.read("config.ini")
bot = commands.Bot(command_prefix='>')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(config["discordbot"]["Token"])
