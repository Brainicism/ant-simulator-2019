from peewee import *
from models.users import Users

class BotCommand:
    def __init__(self, client):
        self.client = client

    def aliases(self):
        return ["join"]

    async def handle(self, message, command, arguments):
        if not Users.select().where((Users.discord_id == message.author.id) & (Users.server_id == message.guild.id)):
	        Users.insert(discord_id=str(message.author.id), server_id=str(message.guild.id)).execute()
	        await message.channel.send('You have joined the game!')
        else:
            await message.channel.send('You have already joined this game.')
