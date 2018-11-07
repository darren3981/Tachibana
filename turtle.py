import discord
import random
from discord.ext import commands

class turtle:
    def __init__(self,client):
        self.client = client

    @commands.group(name='turtle', pass_context=True)
    async def turtle(self, ctx):
        if ctx.invoked_subcommand is None:
            possible_responses = [
                ':ocean::turtle::turtle: A turtle made it to the water!',
                ':skull_crossbones::turtle: :skull_crossbones: lmfao you let a turtle die idiot'
            ]
            turtle_count = ""
            tchoice = (random.choice(possible_responses))
            if tchoice == possible_responses[1]:
                tcount = open('turtle.txt','r+')
                turtle_count = tcount.read()
                turtle_count = str(int(turtle_count) + 1)
                tcount.truncate()
                tcount.seek(0)
                tcount.write(turtle_count)
                tcount.close()
            await self.client.say( tchoice + " " + ctx.message.author.mention)

    @turtle.command(pass_context=True)
    async def count(self, ctx):
        tcount = open('turtle.txt','r')
        turtle_count = tcount.read()
        tcount.close()
        await self.client.say( turtle_count + " turtles have died since creation " + ctx.message.author.mention)

def setup(client):
    client.add_cog(turtle(client))
