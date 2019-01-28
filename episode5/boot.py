import discord
from discord.ext import commands

TOKEN = "" #add your bot token here

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Bot is online.")

#!connect command
@client.command(pass_context=True)
async def connect(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

#!disconnect command
@client.command(pass_context=True)
async def disconnect(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()



client.run(TOKEN)
