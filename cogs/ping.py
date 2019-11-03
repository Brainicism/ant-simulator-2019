from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["pong", "umi"])
    async def ping(self, ctx):
        command = ctx.invoked_with
        if command == "ping":
            await ctx.send("Pong!")
        if command == "pong":
            await ctx.send("Ping!")
        if command == "umi":
            await ctx.send("Bzzzzz")
