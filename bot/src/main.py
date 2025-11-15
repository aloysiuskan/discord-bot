import discord
import os

TOKEN = str(os.getenv("TOKEN"))

bot = discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

bot.run(TOKEN)