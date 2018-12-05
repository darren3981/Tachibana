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
            try:
                info_url = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/characters/' + str(search['character'][0]) + '/?datasource=tranquility'))
                try:
                    Asearch = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/alliances/' + str(info_url['alliance_id']) + '/?datasource=tranquility'))
                except:
                    Asearch = 'Character is not in an Alliance!'
                Csearch = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/corporations/' + str(info_url['corporation_id']) + '/?datasource=tranquility'))
                zdata = json.load(urllib.request.urlopen('https://zkillboard.com/api/stats/characterID/' + str(search['character'][0]) + '/'))
                zlink = 'https://zkillboard.com/character/'+ str(search['character'][0])
                wlink = 'https://evewho.com/pilot/' + url_search   
                embed=discord.Embed(color=0xfa14e9)
                embed.set_thumbnail(url='https://imageserver.eveonline.com/Character/' + str(search['character'][0]) + '_128.jpg')
                try:
                    embed.set_author(name=(info_url['name']), icon_url='https://imageserver.eveonline.com/Alliance/' + str(info_url['alliance_id']) + '_128.png')
                except:
                    embed.set_author(name=(info_url['name']))
                embed.add_field(name='Corporation', value=('Character is in ' + Csearch['name'] + ' (' + Csearch['ticker'] + ')'), inline=False)
                try:
                    embed.add_field(name='Alliance', value=('Character is in ' + Asearch['name'] + ' (' + Asearch['ticker'] + ')'), inline=False)
                except:
                    embed.add_field(name='Alliance', value=(str(Asearch)), inline=False)
                try:
                    embed.add_field(name='Total kills:', value= (zdata['shipsDestroyed']), inline=False)
                    embed.add_field(name='Links', value= '[zkill](' + zlink + ')' + '\n' + '[evewho](' + wlink + ')', inline=False)
                except:
                    embed.add_field(name='Total kills:', value= ('zkill doesn\'t exist'), inline=False)
            except:
                embed=discord.Embed(title= 'character doesn\'t exist or you cant spell (lol)', color=0xfa14e9)
            
                
            await self.client.say(embed=embed)

    @char.command(pass_context=True)
    async def strict(self, ctx):
        message = ctx.message.content
        name = message[14:]
        url_search = urllib.parse.quote(name)
        search = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/search/?categories=character&datasource=tranquility&language=en-us&search=' + url_search + '&strict=true'))
        try:
            info_url = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/characters/' + str(search['character'][0]) + '/?datasource=tranquility'))
            try:
                Asearch = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/alliances/' + str(info_url['alliance_id']) + '/?datasource=tranquility'))
            except:
                Asearch = 'Character is not in an Alliance!'
            Csearch = json.load(urllib.request.urlopen('https://esi.evetech.net/latest/corporations/' + str(info_url['corporation_id']) + '/?datasource=tranquility'))
            zdata = json.load(urllib.request.urlopen('https://zkillboard.com/api/stats/characterID/' + str(search['character'][0]) + '/')) 
            zlink = 'https://zkillboard.com/character/'+ str(search['character'][0])
            wlink = 'https://evewho.com/pilot/' + url_search   
            embed=discord.Embed(color=0xfa14e9)
            embed.set_thumbnail(url='https://imageserver.eveonline.com/Character/' + str(search['character'][0]) + '_128.jpg')
            embed.set_author(name=(info_url['name']), icon_url='https://imageserver.eveonline.com/Alliance/' + str(info_url['alliance_id']) + '_128.png')
            embed.add_field(name='Corporation', value=('Character is in ' + Csearch['name'] + '(' + Csearch['ticker'] + ')'), inline=False)
            try:
                embed.add_field(name='Alliance', value=('Character is in ' + Asearch['name'] + '(' + Asearch['ticker'] + ')'), inline=False)
            except:
                embed.add_field(name='Alliance', value=(str(Asearch)), inline=False)
            try:
                embed.add_field(name='Total kills:', value= (zdata['shipsDestroyed']), inline=False)
                embed.add_field(name='Links', value= '[zkill](' + zlink + ')' + '\n' + '[evewho](' + wlink + ')', inline=False)
                
            except:
                embed.add_field(name='Total kills:', value= (zdata['zkill doesn\'t exist']), inline=False)
                
        except:
            embed=discord.Embed(title= 'character doesn\'t exist or you cant spell (lol)', color=0xfa14e9)
            
        await self.client.say(embed=embed)

def setup(client):
    client.add_cog(Char_search(client))   #adds the cog to the bot
