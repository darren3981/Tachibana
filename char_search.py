import discord
from discord.ext import commands
import aiohttp
import json
from urllib.parse import quote
import urllib.request

class Char_search:
    def __init__(self,client):
        self.client = client
    @commands.group(pass_context=True, hidden=True)
    async def char(self, name):
        search_name = urllib.parse.quote(name)
        urlSn = 'https://esi.evetech.net/latest/search/?categories=character&datasource=tranquility&language=en-us&search=' + search_name + '&strict=false'
        async with aiohttp.ClientSession() as session:  # Async HTTP request
            raw_Sn = await session.get(urlSn)
            Sn = await raw_Sn.text()
            Sn = json.loads(Sn)#Sn is the Character Id
        await self.client.say(str(Sn))

def setup(client):
    client.add_cog(Char_search(client))   #adds the cog to the bot
