import discord
from discord.ext import commands

class Source(commands.Cog):
    """Source of project (github and others)"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['news', 'github', 'source', 'features', 'info'])
    async def _source(self, ctx):
        embed = discord.Embed(title="<a:w_papper:985813363932168233> Source:",
                        description="**<:o_juice_cup:985813346328649739> Hello dear!** \n "
                        "This is an open source discord bot. \n "
                        "You can see source code on [**GitHub**](https://github.com/6eba610ia9/WhiteaBot)! \n",
                        
                        color=0x800080)
        await ctx.send(embed = embed)
        

def setup(bot):
    bot.add_cog(Source(bot))