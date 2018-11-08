import discord
from discord.ext import commands
import json
import urllib.request
from urllib.parse import quote


class Char_search:
    def __init__(self,client):
        self.client = client
    @commands.group(pass_context=True, invoke_without_command=True) # invoke_without_command will only run this command if not sub command is invoked
    async def char(self, ctx):
        if ctx.invoked_subcommand is None:
            message = ctx.message.content
            name = message[7:]
            url_search = urllib.parse.quote(name)
            search = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/search/?categories=character&datasource=tranquility&language=en-us&search=' + url_search + '&strict=false'))
            info_url = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/characters/' + str(search['character'][0]) + '/?datasource=tranquility'))
            zdata = json.load(urllib.request.urlopen('https://zkillboard.com/api/stats/characterID/' + str(search['character'][0]) + '/'))
            try:
                Asearch = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/alliances/' + str(info_url['alliance_id']) + '/?datasource=tranquility'))
            except:
                Asearch = 'Character is not in an Alliance!'
            Csearch = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/corporations/' + str(info_url['corporation_id']) + '/?datasource=tranquility'))
            embed=discord.Embed(title=info_url['name'], color=0xfa14e9)
            embed.set_thumbnail(url='https://imageserver.eveonline.com/Character/' + str(search['character'][0]) + '_128.jpg')
            embed.add_field(name='Corporation', value=('Character is in ' + Csearch['name'] + ' (' + Csearch['ticker'] + ')'), inline=False)
            try:
                embed.add_field(name='Alliance', value=('Character is in ' + Asearch['name'] + ' (' + Asearch['ticker'] + ')'), inline=False)
            except:
                embed.add_field(name='Alliance', value=(str(Asearch)), inline=False)
            try:
                embed.add_field(name='Total kills:', value= (zdata['shipsDestroyed']), inline=False)
            except:
                embed.add_field(name='Total kills:', value= ('zkill deosnt exist'), inline=False)
            
                
            await self.client.say(embed=embed)

    @char.command(pass_context=True)
    async def strict(self, ctx):
        message = ctx.message.content
        name = message[14:]
        url_search = urllib.parse.quote(name)
        search = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/search/?categories=character&datasource=tranquility&language=en-us&search=' + url_search + '&strict=true'))
        info_url = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/characters/' + str(search['character'][0]) + '/?datasource=tranquility'))
        zdata = json.load(urllib.request.urlopen('https://zkillboard.com/api/stats/characterID/' + str(search['character'][0]) + '/'))
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
        try:
            embed.add_field(name='Total kills:', value= (zdata['shipsDestroyed']), inline=False)
        except:
            embed.add_field(name='Total kills:', value= (zdata['zkill deosnt exist']), inline=False)
        
            
        await self.client.say(embed=embed)

def setup(client):
    client.add_cog(Char_search(client))   #adds the cog to the bot
