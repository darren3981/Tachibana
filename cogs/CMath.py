import discord
from discord.ext import commands

class CMath:
    def __init__(self,client):
        self.client = client

    @commands.group(pass_context=True, hidden=True) #commands for math operation
    async def math(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.client.say('You must choose an operation!')

    @math.command(brief="Multiplication of the numbers given.") #multiplies the given numbers
    async def multiply(self, mnumber, mnumber2):
        times_value = float(mnumber) * float(mnumber2)
        await self.client.say(str(mnumber) + ' multiplied by ' + str(mnumber2) + ' is ' + str(times_value))

    @math.command(brief="Division of the numbers given.")   #divides the given numbers
    async def divide(self, dnumber, dnumber2):
        divded_value = float(dnumber) / float(dnumber2)
        await self.client.say(str(dnumber) + ' divided by ' + str(dnumber2) + ' is ' + str(divded_value))

    @math.command(brief="Squares the given number.")    #squares the given numbers
    async def square(self,number):
        squared_value = float(number) * float(number)
        await self.client.say(str(number) + " squared is " + str(squared_value))

    @math.command(brief="Cubes the given number.")      #cubes the given numbers
    async def cube(self,number):
        cubed_value = float(number) * float(number) * float(number)
        await self.client.say(str(number) + " cubed is " + str(cubed_value))

def setup(client):
    client.add_cog(CMath(client))   #adds the cog to the bot
