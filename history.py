import discord
from discord.ext import commands
import aiohttp
import json
import random

class History:
    def __init__(self,client):
        self.client = client
    @commands.command() #command that posts a random historical fact pulled from muffinlabs api
    async def history(self):
        url = 'https://history.muffinlabs.com/date'
        async with aiohttp.ClientSession() as session:  # Async HTTP request
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response) #sets the json api dict as variable named response
            fact = random.choice(list(response['data']['Events']))  # chooses a random fact key from the reponse dict
            embed=discord.Embed(title='Today (' + response['date'] + ') in history!', description=fact['text'] + ' (' + fact['year'] + ')', color=0xfa14e9)
            #embed.add_field(name='Date', value=response['date'], inline=False)
            #embed.add_field(name='Event', value=fact['text'] + ' (' +fact['year'] + ')', inline=False)
            #embed.add_field(name='Wikipedia link', value=fact['Links']['link'][0], inline=False)
            await self.client.say(embed=embed)

def setup(client):
    client.add_cog(History(client)) #adds the cog to the bot
