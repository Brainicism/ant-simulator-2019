import random
import time

from peewee import *
from models.ants import Ants
from models.colony import Colony
from models.users import Users

class BotCommand:
    def __init__(self, client):
        self.client = client

    def aliases(self):
        return ["birth", "egg"]

    async def handle(self, message, command, arguments):
        
        if Users.select().where((Users.discord_id == message.author.id) & (Users.server_id == message.guild.id)):
            num_egg = random.randint(0,10)
            colony_id = Colony.select().where((Colony.discord_id == message.author.id) & (Colony.server_id == message.guild.id)).get()
            eggs = [(colony_id, 'random name', 'random type', 0) for x in range(num_egg)]
            Ants.insert_many(eggs, fields=[Ants.colony_id, Ants.name, Ants.type, Ants.life_stage]).execute()
            await message.channel.send('You have spawned %s egg(s).' % num_egg)
        else:
            await message.channel.send('No queen found.')
