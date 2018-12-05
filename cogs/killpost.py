import discord
from discord.ext import commands
import json
import websockets
import asyncio

class killpost:
    def __init__(self,client):
        self.client = client
    async def killpost(self):
        await self.client.wait_until_ready()
        channel = discord.Object(id='361260764406874132')
        ws = await websockets.connect('wss://zkillboard.com:2096')
        await ws.send("{\"action\":\"sub\",\"channel\":\"alliance:386292982\"}")
        print('now watching for kills!')
        while not self.client.is_closed:
            result = await ws.recv()
            print('received')
            i = json.loads(result)
            print(i['url'])
            if int(i['corporation_id']) == 98456012:
                await self.client.send_message(channel, i['url'])
            await asyncio.sleep(60)