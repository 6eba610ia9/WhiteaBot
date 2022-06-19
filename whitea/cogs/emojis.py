import discord
from discord.ext import commands

class Template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    @commands.command()
    async def emojis(self, ctx):
        
        await ctx.send(discord.Guild.id)

    
def setup(bot):
    bot.add_cog(Template(bot))