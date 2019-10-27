from peewee import *
from models.users import Users

class BotCommand:
    def __init__(self, client):
        self.client = client

    def aliases(self):
        return ["join"]

    async def handle(self, message, command, arguments):
        if command == "join":
            Users.create(discord_id=str(message.author.id), server_id=str(message.guild.id))
            await message.channel.send('You have join the game!')
