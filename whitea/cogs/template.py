import discord
from discord.ext import commands

class Template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    # All you have to add is here:   
    @commands.command()
    async def run(self, ctx, params):
        await ctx.send(params)

    
def setup(bot):
    bot.add_cog(Template(bot))