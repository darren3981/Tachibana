import discord
from discord.ext import commands

class Help:
    def __init__(self,client):
        self.client = client

    @commands.group(pass_context=True, hidden=True)
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            embed=discord.Embed(title="Welcome to the Help command!", description="the bot command is (t.)", color=0xfa14e9 )
            embed.set_thumbnail(url="https://i.imgur.com/4IlgoDu.jpg")
            embed.add_field(name='How to navigate the help command', value='use the modifiers on the end of help to navigate the help commands', inline=False)
            embed.add_field(name='eve', value='displays eve related commands', inline=False)
            embed.add_field(name='fun', value='displays the fun related commands', inline=False)
            embed.add_field(name='tools', value='displays the useful commands', inline=False)
            await self.client.say(embed=embed)
    @help.command()
    async def eve(self):
        embed=discord.Embed(title="Eve commands!", description="the bot command is (t.)", color=0xfa14e9 )
        embed.set_thumbnail(url="https://i.imgur.com/4IlgoDu.jpg")
        embed.add_field(name='plex', value='displays the current value of plex', inline=False)
        embed.add_field(name='char', value='post corp and alliance of character provided', inline=False)
        embed.add_field(name='range', value='post dotland range links from given system', inline=False)
        await self.client.say(embed=embed)
    @help.command()
    async def fun(self):
        embed=discord.Embed(title="Fun commands!", description="the bot command is (t.)", color=0xfa14e9 )
        embed.set_thumbnail(url="https://i.imgur.com/4IlgoDu.jpg")
        embed.add_field(name='turtle', value='help the turtle get to the water!', inline=False)
        embed.add_field(name='8ball', value='invoke the great wisdom of Tachibana', inline=False)
        embed.add_field(name='catgirl', value='posts a cute catgirl! Modifiers: nsfw', inline=True)
        embed.add_field(name='history', value='displays a random history fact that happened on the current date', inline=False)
        await self.client.say(embed=embed)
    @help.command()
    async def tools(self):
        embed=discord.Embed(title="Tool commands!", description="the bot command is (t.)", color=0xfa14e9 )
        embed.set_thumbnail(url="https://i.imgur.com/4IlgoDu.jpg")
        embed.add_field(name='bitcoin', value='displays the current value of bitcoin in USD and EUR', inline=False)
        embed.add_field(name='weather', value='displays the current weather for the given location', inline=False)
        await self.client.say(embed=embed)

def setup(client):
    client.add_cog(Help(client))
