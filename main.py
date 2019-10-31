import discord
import configparser
from models.ants import Ants
from models.colony import Colony
from models.forage_events import ForageEvents
from models.species import Species
from models.users import Users
from discord.ext import commands
from peewee import *
from os.path import dirname, basename
import importlib.util
import os
from cogs.game import Game
from cogs.leave import Leave
from cogs.birth import Birth
from cogs.ping import Ping

print("Reading config...")
config = configparser.ConfigParser()
config.read("config.ini")

bot = commands.Bot(command_prefix=config["discordbot"]["CommandPrefix"], description='A Rewrite Cog Example')
bot.add_cog(Game(bot))
bot.add_cog(Birth(bot))
bot.add_cog(Ping(bot))

print("Starting database...")
db = SqliteDatabase('main.db')
db.connect()
db.create_tables([Ants, Colony, Species, ForageEvents, Users])

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

bot.run(config["discordbot"]["Token"])
