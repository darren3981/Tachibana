import discord
from discord.ext import commands
import aiohttp
import json

class PLEX:
    def __init__(self,client):
        self.client = client
    @commands.command(brief="Displays the current value of plex.")
    async def plex(self):
        url = 'https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id=44992'
        async with aiohttp.ClientSession() as session:  # Async HTTP request
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            output_list = [x['price'] for x in response]
            min_price = min(output_list)
            embed=discord.Embed(title='PLEX Price', color=0xfa14e9)
            embed.set_thumbnail(url="https://web.ccpgamescdn.com/secure/images/plex/plex-icon-110.png")
            embed.add_field(name='current price of plex', value=str(('{:,}'.format(min_price)) ) + ' isk', inline=False)
            embed.add_field(name='current price of plex x500', value=str('{:,}'.format(min_price * 500)) + ' isk', inline=False)
            
            await self.client.say(embed=embed)
            #print(response)
            

def setup(client):
    client.add_cog(PLEX(client))
