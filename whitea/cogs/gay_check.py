import discord
from discord.ext import commands
import random

class Template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    # All you have to add is here:   
    @commands.command()
    async def gay(self, ctx):
        procents = random.randint(0,100)
        embed = discord.Embed(colour=0x428DFF, 
                       description=f" {ctx.author.name} is {procents}% gay lol")
        message = await ctx.send(embed = embed)
        await message.add_reaction("🏳️‍🌈")
    
def setup(bot):
    bot.add_cog(Template(bot))