import discord
from discord.ext import commands
import aiohttp
import json
import urllib.request
from urllib.parse import quote

class Price:
    def __init__(self,client):
        self.client = client
    @commands.group(pass_context=True, invoke_without_command=True) # invoke_without_command will only run this command if not sub command is invoked
    async def price(self, ctx):
        if ctx.invoked_subcommand is None:
            message = ctx.message.content
            name = message[8:]
            url_search = urllib.parse.quote(name)
            search = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/search/?categories=inventory_type&datasource=tranquility&language=en-us&search=' + str(url_search) + '&strict=true'))
            info_url = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id=' + str(search['inventory_type'][0])))
            output_list = [x['price'] for x in info_url]
            min_price = min(output_list)
            embed=discord.Embed(title= name +' Price', color=0xfa14e9)
            embed.set_thumbnail(url='https://imageserver.eveonline.com/Type/' + str(search['inventory_type'][0]) + '_64.png')
            embed.add_field(name='current price' , value=str(('{:,}'.format(min_price)) ) + ' isk', inline=False)
            await self.client.say(embed=embed)
            

def setup(client):
    client.add_cog(Price(client))
