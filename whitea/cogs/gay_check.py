import discord
from discord.ext import commands
import random

class Template(commands.Cog):
    """Return a random procent of lgbt rate"""
    def __init__(self, bot):
        self.bot = bot
       
    # All you have to add is here:   
    @commands.command()
    
    async def gay(self, message, member=None):
        procents = random.randint(0, 101)
        if member is None:
            embed = discord.Embed(colour=discord.Colour.random(), 
                        description=f"You are {procents}% gay")
            message = await message.send(embed = embed)
            await message.add_reaction("🏳️‍🌈")
        else:
            embed = discord.Embed(colour=discord.Colour.random(), 
                        description=f"{member} is {procents}% gay lol")
            message = await message.send(embed = embed)
            await message.add_reaction("🏳️‍🌈")
    
def setup(bot):
    bot.add_cog(Template(bot))