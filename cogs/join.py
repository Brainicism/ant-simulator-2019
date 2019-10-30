import random

from peewee import *
from models.ants import Ants
from models.colony import Colony
from models.users import Users
from discord.ext import commands

class Join(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        species = ['Camponotus', 'Yellow Crazy Ants']
        message = ctx.message
        if not Users.select().where((Users.discord_id == message.author.id) & (Users.server_id == message.guild.id)):
            user_id = Users.insert(discord_id=str(message.author.id), server_id=str(message.guild.id)).execute()
            colony_id = Colony.insert(
                user_id=user_id,
                species_id=species.id,
                colony_name=message.author.name + '\'s Colony',
                current_food_supply=100,
                max_food_supply=100
            ).execute()
            Ants.insert(
                colony_id=colony_id,
                name='sdfsdfsdf',
                role='queen',
                life_stage=3
            ).execute()
            await message.channel.send('You have joined the game!')
        else:
            await message.channel.send('You have already joined this game.')
