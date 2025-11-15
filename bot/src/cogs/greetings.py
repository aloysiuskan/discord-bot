import discord
from discord.ext import commands
import yaml

class Greetings(commands.Cog):   

    def __init__(self,bot):
        self.bot = bot
        with open("/usr/local/app/config.yaml", "r") as file:
            self.config = yaml.safe_load(file)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(
            title = self.config["greetings"]["welcome_title"].format(member = member),
            description = self.config["greetings"]["welcome_message"].format(member=member)
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        await member.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        embed = discord.Embed(
            title = self.config["greetings"]["goodbye_title"].format(member = member),
            description = self.config["greetings"]["goodbye_message"].format(member = member)
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        await member.send(embed=embed)

    
    
def setup(bot):
    bot.add_cog(Greetings(bot))