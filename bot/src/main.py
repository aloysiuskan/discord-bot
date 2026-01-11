import discord
import os

TOKEN = str(os.getenv("TOKEN"))

bot = discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

cogs_list = ["greetings","utils"]

for cog in cogs_list:
    bot.load_extension(f"cogs.{cog}")

bot.run(TOKEN)