import discord
from discord.ext import commands

TOKEN = "" #Add your token here

client = commands.Bot(command_prefix = "!")
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot is online")


@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")


client.run(TOKEN)
