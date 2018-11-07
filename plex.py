import discord
from discord.ext import commands
import json
import urllib.request

class PLEX:
    def __init__(self,client):
        self.client = client
    @commands.command()
    async def plex(self):
        data = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id=44992')) #api pull for prices of plex
        output_list = [x['price'] for x in data] #pulls all prices into single array
        min_price = min(output_list)    #sorts for the lowest price returns
        embed=discord.Embed(title='PLEX Price', color=0xfa14e9) #embed set up
        embed.set_thumbnail(url="https://web.ccpgamescdn.com/secure/images/plex/plex-icon-110.png")
        embed.add_field(name='current price of plex', value=str(min_price) + 'm isk', inline=False)
        embed.add_field(name='current price of plex x500', value=str(min_price * 500) + 'm isk', inline=False)
        await self.client.say(embed=embed)
                
def setup(client):  #sets up cog
    client.add_cog(PLEX(client))
