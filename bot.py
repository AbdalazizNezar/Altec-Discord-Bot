import discord
from discord.ext import commands

BOT_NAME = "Altec" #Change this into whatever you want.

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"{BOT_NAME} is online!")


bot.run(TOKEN)
