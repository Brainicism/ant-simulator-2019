import random
import time
import names

from peewee import *
from models.ants import Ants
from models.colony import Colony
from models.users import Users
from discord.ext import commands

class Birth(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["egg"])
    async def birth(self, ctx):
        message = ctx.message
        user_id = Users.get_or_none((Users.discord_id == message.author.id) & (Users.server_id == message.guild.id)).id;
        if user_id is not None:
            num_egg = random.randint(0,10)
            colony_id = Colony.get(Colony.user == user_id).id
            eggs = [(colony_id, names.get_full_name(), "random type", 0) for x in range(num_egg)]
            Ants.insert_many(eggs, fields=[Ants.colony, Ants.name, Ants.role, Ants.life_stage]).execute()
            await message.channel.send("You have spawned %s egg(s)." % num_egg)
        else:
            await message.channel.send("No queen found.")
