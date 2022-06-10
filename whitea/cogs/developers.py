import discord
from discord.ext import commands

class Developers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    
    @commands.command()
    async def zet(self, ctx):
        """Zet"""
        zet =  discord.Embed(title="Support Developer ❤️",
                            description="Follow on  [Insta]("
                                        "https://www.instagram.com/justzetu/) 👀", color=0x89CFF0)
        await ctx.send(embed=zet)

    @commands.command()
    async def sebastian(self, ctx):
        """Sebastian"""
        sebastian =  discord.Embed(title="Support Developer ❤️",
                            description="Follow on [Insta]("
                                        "https://www.instagram.com/sebasti4n.exe/) ❤️", color=0x89CFF0)
        await ctx.send(embed=sebastian)

    
def setup(bot):
    bot.add_cog(Developers(bot))