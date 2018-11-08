from datetime import datetime
from pytz import timezone
import pytz
import discord
from discord.ext import commands

class ETime:
    def __init__(self,client):
        self.client = client

    @commands.command() #displays the current time
    async def time(self):
        cst = datetime.now(timezone('America/Chicago')) #sets variable for CST tz
        utc = datetime.now(timezone('Etc/UTC')) #sets variable for UTC tz
        embed=discord.Embed(title="Current Time", description="", color=0xfa14e9)
        embed.add_field(name='CST:', value=('%02d:%02d:%02d   %02d/%02d/%04d' % (cst.hour, cst.minute, cst.second, cst.month, cst.day, cst.year)), inline=False)
        embed.add_field(name='UTC:', value=('%02d:%02d:%02d   %02d/%02d/%04d' % (utc.hour, utc.minute, utc.second, utc.month, utc.day, utc.year)), inline=True)
        await self.client.say(embed=embed)

def setup(client):
    client.add_cog(ETime(client))   #adds the cog to the bot
