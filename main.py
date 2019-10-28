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

print("Reading config...")
config = configparser.ConfigParser()
config.read("config.ini")

bot = discord.Client()

commands = {}
for command_file in [file for file in os.listdir("commands") if file.endswith(".py")]:
    command_file_path = os.path.join("commands", command_file)
    command_name = command_file[:-3]

    spec = importlib.util.spec_from_file_location(command_name, command_file_path)
    botCommandSpec = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(botCommandSpec)
    botCommandInstance = botCommandSpec.BotCommand(bot)
    for alias in botCommandInstance.aliases():
        commands[alias] = botCommandInstance
    print("Loaded plugin: " + basename(command_file_path))

print("Starting database...")
db = SqliteDatabase('main.db')
db.connect()
db.create_tables([Ants, Colony, Species, ForageEvents, Users])


@bot.event
async def on_message(message):
    #TODO: move this logic into some sort of command processor
    if message.content.startswith(config["discordbot"]["CommandPrefix"]):
        words = message.content.partition(' ')
        requested_command = words[0][1:]
        if requested_command in commands:
            await commands[requested_command].handle(message, requested_command, words[1:])


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

bot.run(config["discordbot"]["Token"])
