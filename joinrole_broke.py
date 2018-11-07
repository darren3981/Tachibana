import asyncio
import logging
#import requests
import traceback

from discord.embeds import Embed
from discord.ext import commands
from discord.utils import get


class JoinRole:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def roles(self, ctx):

        embed = Embed(
            title=f'Currently available optional roles in {ctx.guild.name}: o.join <role name>')
        with open('cogs/utils/roles.txt', encoding='utf8') as rolef:
            rolesList = rolef.read().splitlines()
            for role in rolesList:
                embed.add_field(
                    name=role, value=f'Grants {role} role', inline=False)
        return await ctx.send(embed=embed)
# at some point, add a catch to give a response if a user already has a requested role

    @commands.command()
    async def join(self, ctx, *, role):
        with open('cogs/utils/roles.txt', encoding='utf8') as rolef:
            rolesList = rolef.read().splitlines()
        print(ctx.message.author.roles)
        if role not in rolesList:
            return await ctx.message.add_reaction(chr(0x274c))

        else:
            roleGet = get(ctx.guild.roles, name=f'{role}')
            await ctx.message.author.add_roles(roleGet)
            return await ctx.message.add_reaction(chr(0x1f44d))

    @commands.command()
    async def leave(self, ctx, *, role):
        with open('cogs/utils/roles.txt', encoding='utf8') as rolef:
            rolesList = rolef.read().splitlines()
        if role not in rolesList:
            return await ctx.message.add_reaction(chr(0x274c))

        else:
            roleGet = get(ctx.guild.roles, name=f'{role}')
            await ctx.message.author.remove_roles(roleGet)
            return await ctx.message.add_reaction(chr(0x1f44d))


def setup(client):
    client.add_cog(JoinRole(client))
