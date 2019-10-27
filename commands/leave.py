from peewee import *
from models.users import Users

class BotCommand:
    def __init__(self, client):
        self.client = client

    def aliases(self):
        return ["leave"]

    async def handle(self, message, command, arguments):
        if Users.select().where((Users.discord_id == message.author.id) & (Users.server_id == message.guild.id)):
	        Users.get((Users.discord_id == message.author.id) & (Users.server_id == message.guild.id)).delete_instance()
	        await message.channel.send('You have killed your queen ant.')
        else:
            await message.channel.send('You are not a part of this game.')
