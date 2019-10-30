import discord
import configparser
from models.ants import Ants
from models.colony import Colony
from models.forage_events import ForageEvents
from models.species import Species
from models.users import Users
from discord.ext import commands
import seed
from peewee import *
from os.path import dirname, basename
import importlib.util
import os
from cogs.join import Join
from cogs.leave import Leave
from cogs.birth import Birth
from cogs.ping import Ping

print("Reading config...")
config = configparser.ConfigParser()
config.read("config.ini")

bot = commands.Bot(command_prefix=config["discordbot"]["CommandPrefix"], description='A Rewrite Cog Example')
bot.add_cog(Join(bot))
bot.add_cog(Leave(bot))
bot.add_cog(Birth(bot))
bot.add_cog(Ping(bot))

print("Starting database...")

import os.path
if not os.path.isfile("main.db"):
    seed.seed()
db = SqliteDatabase('main.db')
db.connect()
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

bot.run(config["discordbot"]["Token"])
