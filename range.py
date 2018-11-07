import discord
from discord.ext import commands
import json
import urllib.request
from urllib.parse import quote


class Range:
    def __init__(self,client):
        self.client = client
    @commands.group(pass_context=True, hidden=True)
    async def range(self, context):
        message = context.message.content
        sname = message[8:]
        search = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/search/?categories=solar_system&datasource=tranquility&language=en-us&search=' + sname + '&strict=false')) #searchs for system name for system id        #print(search['solar_system'][0])
        search_name = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/universe/systems/' + str(search['solar_system'][0]) + '/?datasource=tranquility&language=en-us')) #pulls proper system name based of system id
        system = search_name['name'] 
        range_cap = 'http://evemaps.dotlan.net/range/Thanatos,5/' + str(system) #adds system name to dotlan urls
        range_super = 'http://evemaps.dotlan.net/range/Nyx,5/' + str(system)
        await self.client.say('the range for caps is ' + range_cap)
        await self.client.say('the range for supers is ' + range_super)

def setup(client):
    client.add_cog(Range(client))   #adds the cog to the bot
