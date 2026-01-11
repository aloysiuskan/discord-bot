import discord
from discord.ext import commands
import random

class Utils(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="dice", description="Roll a standard 6-face dice")
    async def dice(self, ctx):
        await ctx.respond(random.randrange(1,7))

    @discord.slash_command(name="custom_dice", description="Roll a k-face dice n times")
    async def custom_dice(self, ctx, k:discord.Option(int, description="Number of faces", min_value=1, max_value=100), n:discord.Option(int, description="Number of times", min_value=0, max_value=100)):
        result = ""
        total = 0
        for _ in range(n):
            dice_result = random.randrange(1,k+1)
            result += str(dice_result) + " "
            total += dice_result
        await ctx.respond("Result:\n" + result + "\nSum: " + str(total))

        

def setup(bot):
    bot.add_cog(Utils(bot))
