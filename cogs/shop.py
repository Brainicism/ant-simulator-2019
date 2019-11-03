from peewee import *
from models.shop_items import Shop_items
from discord.ext import commands

class Shop(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["browse"])
    async def shop(self, ctx):
        message = ctx.message
        await message.channel.send("".join(['Name     Price\n'] + [x.name + " " + str(x.price) + "\n" for x in Shop_items.select()]))
