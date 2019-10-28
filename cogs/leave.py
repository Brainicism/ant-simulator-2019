from peewee import *
from models.users import Users
from discord.ext import commands

class Leave(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def leave(self, ctx):
        message = ctx.message
        if Users.select().where((Users.discord_id == message.author.id) & (Users.server_id == message.guild.id)):
	        Users.delete().where((Users.discord_id == message.author.id) & (Users.server_id == message.guild.id)).execute()
	        await ctx.send('You have killed your queen ant.')
        else:
            await ctx.send('You are not a part of this game.')
