import discord
from discord.ext import commands

class Template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    @commands.command()
    async def support(self, ctx):
        embed = discord.Embed(title="<:p_coffies:985813365739892756> Support:",
                        description="**<:o_juice_cup:985813346328649739> If you want to support whitea:** \n \n"
                        "<:o_juice:985813374875086858>  Make sure you [**vote**](https://top.gg/bot/982162391318036520/vote). \n "
                        "<:g_sended:984970341069774928> Join on [**support server**](https://discord.gg/TbpjY89AtU) \n \n"
                        
                        "**Thank's!**",
                        color=0x800080)
        await ctx.send(embed = embed)

    
def setup(bot):
    bot.add_cog(Template(bot))