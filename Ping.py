import discord
from discord.ext import commands

class Ping:
    def __init__(self,client):
        self.client = client

    #async def on_message_delete(self, message):
        #await self.client.send_message(message.channel, 'Message deleted.')

    @commands.command(pass_context=True)
    async def ping(self, context):
        await self.client.say(context.message.author.mention + " Pong! :ping_pong:")

def setup(client):
    client.add_cog(Ping(client))
