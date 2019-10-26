import discord
import configparser
from models.ant import Ant
from models.colony import Colony
from discord.ext import commands
from peewee import *

print("Reading config...")
config = configparser.ConfigParser()
config.read("config.ini")

bot = commands.Bot(command_prefix='>')

print("Starting database...")
db = SqliteDatabase('main.db')
db.connect()
db.create_tables([Ant, Colony])


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

bot.run(config["discordbot"]["Token"])
