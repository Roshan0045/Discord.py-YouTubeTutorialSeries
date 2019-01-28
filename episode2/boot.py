import discord
from discord.ext import commands
import asyncio
from itertools import cycle

TOKEN = "" #Add your bot token here

client = commands.Bot(command_prefix = "!")

statusmsg = ['SingleMessage'] #Status Messages

#status
async def change_status():
        await client.wait_until_ready()
        messages = cycle(statusmsg)

        while not client.is_closed:
                current_status = next(messages)
                await client.change_presence(game=discord.Game(name=current_status))
                await asyncio.sleep(4) #How long it will wait until changing the statusmsg


@client.event
async def on_ready():
    print("Bot is online")

client.loop.create_task(change_status())
client.run(TOKEN)
