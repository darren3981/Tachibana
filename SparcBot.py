import discord
import asyncio
from discord import Game
from discord.ext import commands

#TOKEN = 'token goes in discord_token file'
client = commands.Bot(command_prefix = "s.")#sets the bot command prefix to s.

client.remove_command('help')# removes the default discord.py help command to replace with custom help command

extensions = ['eightballt', 'Ping', 'bitcoin', 'ETime', 'CMath', 'turtle', 'weather', 'catgirl', 'help', 'plex2', 'history']

@client.event #sets the bot status and prints servers bot is in every 10 minutes
async def on_ready():
    await client.change_presence(game=Game(name="with your waifu"))
    print('Bot Online.')
    print("Logged in as " + client.user.name)
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)
        
@client.command()
async def load(extension):#command that allows loading of extensions after start up
    try:
        client.load_extension(extension)
        print('Loaded {}')
    except Exception as error:
        print('{} connot be loaded.[{}]'.format(extension, error))

@client.command()
async def unload(extension):#command that allows unloading of extensions after start up
    try:
        client.unload_extension(extension)
        print('Unloaded {}')
    except Exception as error:
        print('{} connot be unloaded.[{}]'.format(extension, error))

@client.command()
async def reload(extension):#command that allow reloading of extensions after start up
    try:
        client.unload_extension(extension)
        client.load_extension(extension)
        print('Unloaded {}')
        print('Loaded {}')
    except Exception as error:
        print('{} connot be reloaded.[{}]'.format(extension, error))

#@client.command(pass_context = True)
#async def clear(ctx, number):
#    mgs = [] #Empty list to put all the messages in the log
#    number = int(number) #Converting the amount of messages to delete to an integer
#    async for x in client.logs_from(ctx.message.channel, limit = number):
#        mgs.append(x)
#    await client.delete_messages(mgs)

if __name__ == '__main__':# sets file as main and starts bot
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} connot be loaded.[{}]'.format(extension,error))
    with open('sparc_token.txt','r') as f:
        key = f.readline()
    client.run(key)
