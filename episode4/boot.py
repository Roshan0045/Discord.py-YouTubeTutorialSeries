import discord
from discord.ext import commands


TOKEN = "" #Add your bot token here

client = commands.Bot(command_prefix = "!")
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot is online")

#Help Command
@client.command(pass_context=True)
async def help(ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Colour.purple() #Colour on the side of the discord Embed
        )

        embed.set_author(name="YouTube Test Bot - Help and Documentation")
        embed.add_field(name="!help", value="Your using it right now!", inline=False)
        embed.add_field(name="Subscribe", value="https://youtube.com/c/m692onyt", inline=False)

        await client.send_message(author, embed=embed)
        await client.say("Message sent to your DMs! :thumbsup:")


client.run(TOKEN)
