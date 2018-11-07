import asyncio
import aiohttp
import json

import traceback
import urllib.request
import discord
import requests
from discord import embeds
from discord.colour import Color
from discord.ext import commands


class Catgirl:
    def __init__(self, client):
        self.client = client

    @commands.group(pass_context=True, hidden=True) #command the imports a random img from api
    async def catgirl(self, ctx):
        if ctx.invoked_subcommand is None:  #checks for a sub-command if defined            
            url = 'https://nekos.moe/api/v1/random/image?nsfw=false'
            async with aiohttp.ClientSession() as session:
                raw_neko = await session.get(url)
                neko = await raw_neko.text()
                neko = json.loads(neko)
                imgURL = 'https://nekos.moe/image/' + neko['images'][0]['id']   #sets the varible as the random url from the api
            embed = embeds.Embed(title='Here\'s a super cute cat girl!', url=imgURL)
            embed.color = 0xfa14e9
            embed.set_image(url=imgURL)
            return await  self.client.say(embed=embed)  #posts the embed

    @catgirl.command(pass_context=True, hidden=True)    #adds the nsfw flag to the img api before chosing random picture
    async def nsfw(self, ctx):
            url = 'https://nekos.moe/api/v1/random/image?nsfw=true'
            async with aiohttp.ClientSession() as session:
                raw_neko = await session.get(url)
                neko = await raw_neko.text()
                neko = json.loads(neko)
                imgURL = 'https://nekos.moe/image/' + neko['images'][0]['id']   #sets the varible as the random url from the api
            embed = embeds.Embed(title='Here\'s a super cute nsfw cat girl!', url=imgURL)
            embed.color = 0xfa14e9
            embed.set_image(url=imgURL)
            return await  self.client.say(embed=embed)  #posts the embed

def setup(client):
    client.add_cog(Catgirl(client)) #adds the cog to the bot
