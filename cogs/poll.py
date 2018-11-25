import discord
from discord.ext import commands


class Poll:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def poll(self, ctx, question, *options: str):
        if len(options) <= 1:
            await self.client.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await self.client.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['✅', '❌']
        else:
            reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=question, description=''.join(description), color=0xfa14e9)
        react_message = await self.client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await self.client.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await self.client.edit_message(react_message, embed=embed)

def setup(client):
    client.add_cog(Poll(client))
