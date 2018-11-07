import discord
from discord.ext import commands
import json
import urllib.request
from urllib.parse import quote


class Char_search:
    def __init__(self,client):
        self.client = client
    @commands.group(pass_context=True, hidden=True)
    async def char(self, context):
        message = context.message.content
        name = message[7:]
        url_search = urllib.parse.quote(name)
        search = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/search/?categories=character&datasource=tranquility&language=en-us&search=' + url_search + '&strict=false'))
        info_url = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/characters/' + str(search['character'][0]) + '/?datasource=tranquility'))
        try:
            Asearch = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/alliances/' + str(info_url['alliance_id']) + '/?datasource=tranquility'))
        except:
            Asearch = 'Character is not in an Alliance!'
        Csearch = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/corporations/' + str(info_url['corporation_id']) + '/?datasource=tranquility'))
        
        embed=discord.Embed(title=info_url['name'], color=0xfa14e9)
        embed.set_thumbnail(url='https://imageserver.eveonline.com/Character/' + str(search['character'][0]) + '_128.jpg')
        embed.add_field(name='Corporation', value=('Character is in ' + Csearch['name'] + '(' + Csearch['ticker'] + ')'), inline=False)
        try:
            embed.add_field(name='Alliance', value=('Character is in ' + Asearch['name'] + '(' + Asearch['ticker'] + ')'), inline=False)
        except:
             embed.add_field(name='Alliance', value=(str(Asearch)), inline=False)
        
            
        await self.client.say(embed=embed)

def setup(client):
    client.add_cog(Char_search(client))   #adds the cog to the bot
