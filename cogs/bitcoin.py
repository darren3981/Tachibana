import discord
from discord.ext import commands
import aiohttp
import json

class Bitcoin:
    def __init__(self,client):
        self.client = client
    @commands.command() #displays current price of bitcoin via coindesk api
    async def bitcoin(self):
        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        async with aiohttp.ClientSession() as session:  #Async HTTP request
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response) #sets reponse variable as the json api dict
            embed=discord.Embed(title='Bitcoin Price', description='current bitcoin prices', color=0xf7931a)
            embed.set_thumbnail(url="https://en.bitcoin.it/w/images/en/2/29/BC_Logo_.png")
            embed.add_field(name='current USD price', value='$' + response['bpi']['USD']['rate'], inline=False)
            embed.add_field(name='current EUR price', value='€' + response['bpi']['EUR']['rate'], inline=True)
            await self.client.say(embed=embed)  #prints the discord embed

def setup(client):
    client.add_cog(Bitcoin(client)) #adds the cog to the bot
