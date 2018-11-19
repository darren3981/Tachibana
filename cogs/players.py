import discord
from discord.ext import commands
import aiohttp
import json
import urllib.request

class Players:
    def __init__(self,client):
        self.client = client
    @commands.group(pass_context=True)
    async def players(self, ctx):
        query = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/status/?datasource=tranquility'))   
        embed=discord.Embed(title="Current players online", description=query['players'], color=0xfa14e9)  
        await self.client.say(embed=embed)
def setup(client):
    client.add_cog(Players(client))
