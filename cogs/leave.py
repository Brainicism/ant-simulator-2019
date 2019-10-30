from peewee import *
from models.ants import Ants
from models.colony import Colony
from models.users import Users
from discord.ext import commands

class Leave(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def leave(self, ctx):
        message = ctx.message
        if Users.select().where((Users.discord_id == message.author.id) & (Users.server_id == message.guild.id)):
            # Deleting everything related to the user might be iffy
            #colony_id = Colony.select().where((Colony.discord_id == message.author.id) & (Colony.server_id == message.guild.id)).get()
            #Ants.delete().where(Ants.colony_id == colony_id).execute()
            #Colony.delete().where((Colony.discord_id == message.author.id) & (Colony.server_id == message.guild.id)).execute()
            Users.delete().where((Users.discord_id == message.author.id) & (Users.server_id == message.guild.id)).execute()
            await message.channel.send('You have killed your queen ant.')
        else:
            await ctx.send('You are not a part of this game.')
