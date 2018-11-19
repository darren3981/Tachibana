import discord
from discord.ext import commands
import json
import urllib.request
from urllib.parse import quote


class Route:
    def __init__(self,client):
        self.client = client
    @commands.group(pass_context=True, hidden=True)
    async def route(self, context, sname, sname2):
        search = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/search/?categories=solar_system&datasource=tranquility&language=en-us&search=' + sname + '&strict=false')) #searchs for system name for system id  
        search_name = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/universe/systems/' + str(search['solar_system'][0]) + '/?datasource=tranquility&language=en-us')) #pulls proper system name based of system id
        search2 = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/search/?categories=solar_system&datasource=tranquility&language=en-us&search=' + sname2 + '&strict=false'))
        search_name2 = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/universe/systems/' + str(search2['solar_system'][0]) + '/?datasource=tranquility&language=en-us'))
        system = search_name['name'] 
        system2 = search_name2['name'] 
        range_cap = 'http://evemaps.dotlan.net/jump/Thanatos,545,S/' + str(system) + ':' + str(system2) #adds system name to dotlan urls 
        range_super = 'http://evemaps.dotlan.net/jump/Nyx,545,S/' + str(system) + ':' + str(system2)
        range_blops = 'http://evemaps.dotlan.net/jump/Panther,545,S/' + str(system) + ':' + str(system2)
        range_jf = 'http://evemaps.dotlan.net/jump/Ark,545,S/' + str(system) + ':' + str(system2)
        embed=discord.Embed(title='Jump routes from ' + system + ' to ' + system2, color=0xfa14e9)
        embed.add_field(name='Capital', value= range_cap, inline=False)
        embed.add_field(name='Supers', value=range_super, inline=False)
        embed.add_field(name='Blops', value=range_blops, inline=False)
        embed.add_field(name='JF', value=range_jf, inline=False)
        await self.client.say(embed=embed)

def setup(client):
    client.add_cog(Route(client))   #adds the cog to the bot
