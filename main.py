import configparser
import importlib.util
import os
import os.path
import threading
import time
from os.path import basename, dirname

import discord
import schedule
from discord.ext import commands
from peewee import *

import seed
from cogs.birth import Birth
from cogs.game import Game
from cogs.shop import Shop
from cogs.ping import Ping
from event_loop import trigger
from models.ants import Ants
from models.colony import Colony
from models.forage_events import ForageEvents
from models.shop_items import ShopItems
from models.species import Species
from models.users import Users

print("Reading config...")
config = configparser.ConfigParser()
config.read("config.ini")

bot = commands.Bot(command_prefix=config["discordbot"]["CommandPrefix"])
bot.add_cog(Game(bot))
bot.add_cog(Birth(bot))
bot.add_cog(Shop(bot))
bot.add_cog(Ping(bot))

print("Starting database...")

seed.seed()
db = SqliteDatabase("main.db")
db.connect()
@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)


def run_event_loop():
    schedule.every(10).minutes.do(trigger, client=bot)
    while True:
        schedule.run_pending()
        time.sleep(1)

t = threading.Thread(target=run_event_loop).start()
bot.run(config["discordbot"]["Token"])
