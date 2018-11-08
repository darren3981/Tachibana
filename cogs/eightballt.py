import discord
import random
from discord.ext import commands

class eightball:
    def __init__(self,client):
        self.client = client

    @commands.command(pass_context=True,name='8ball',aliases=['eight_ball', 'eightball', '8-ball'])    # takes the given text and replies with a random reponse from array
    async def eight_ball(self,context):
        possible_responses = [
            'That is a resounding no',
            'It is not looking likely',
            'Too hard to tell',
            'It is quite possible',
            'Definitely',
            "Shut up and stop breathing",
            "Why were you born again?",
            "Ur gay pwnd lol",
            "probs lol",
            "Yes",
            "No",
            "IDK",
            "Sure!",
            "Nah"
        ]
        message = context.message.content
        question = message[7:]

        embed=discord.Embed(color=0xfa14e9)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/8_ball_icon.svg/2000px-8_ball_icon.svg.png")
        embed.add_field(name=context.message.author.name + ' asked:', value=question, inline=False)
        embed.add_field(name='Tachibana says:', value=random.choice(possible_responses), inline=False)
        await self.client.say(embed=embed)

def setup(client):
    client.add_cog(eightball(client))   #adds the cog to the bot
