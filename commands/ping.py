class BotCommand:
    def __init__(self, client):
        self.client = client

    def aliases(self):
        return ["ping", "pong"]

    async def handle(self, message, command, arguments):
        if command == "ping":
            await message.channel.send("Pong!")
        if command == "pong":
            await message.channel.send("Ping!")