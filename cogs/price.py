import discord
from discord.ext import commands
import aiohttp
import json
import urllib.request
from urllib.parse import quote

class Price:
    def __init__(self,client):
        self.client = client
    @commands.group(pass_context=True)
    async def price(self, ctx, item):        
        url_search = urllib.parse.quote(str(item))
        try:
            search = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/search/?categories=inventory_type&datasource=tranquility&language=en-us&search=' + str(url_search) + '&strict=true'))
            info_url = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id=' + str(search['inventory_type'][0])))
            output_list = [x['price'] for x in info_url]
            min_price = min(output_list)
            embed=discord.Embed(title= str(item) +' Price', color=0xfa14e9)
            embed.set_thumbnail(url='https://imageserver.eveonline.com/Type/' + str(search['inventory_type'][0]) + '_64.png')
            embed.add_field(name='current price' , value=str(('{:,}'.format(min_price)) ) + ' isk', inline=False)
        except:
            embed=discord.Embed(title= 'item doesnt exist or you cant spell (lol)', color=0xfa14e9)        
        await self.client.say(embed=embed)
def setup(client):
    client.add_cog(Price(client))
