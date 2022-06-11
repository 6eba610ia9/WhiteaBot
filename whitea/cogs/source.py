import discord
from discord.ext import commands

class Source(commands.Cog):
    """Source of project (github and others)"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['news', 'github', 'source', 'features', 'info'])
    async def _source(self, ctx):
        embed = discord.Embed(title="⏲ This feature is work in progress!",
                        description="Please stay tuned to our latest updates [here]("
                                     "https://github.com/6eba610ia9/WhiteaBot)!", 
                        color=0x89CFF0)
        await ctx.send(embed = embed)
        

def setup(bot):
    bot.add_cog(Source(bot))