import discord
from discord.ext import commands

class Developers(commands.Cog):
    """About bot developers"""
    def __init__(self, bot):
        self.bot = bot
       
    
    @commands.command()
    async def zet(self, message):
        """Zet"""
        zet =  discord.Embed(title="Support Developer ❤️",
                            description="Follow on  [Insta]("
                                        "https://www.instagram.com/justzetu/) 👀", 
                                        color=discord.Colour.random())
        await message.send(embed=zet)

    @commands.command()
    async def sebastian(self, message):
        """Sebastian"""
        sebastian =  discord.Embed(title="Support Developer ❤️",
                            description="Follow on [Insta]("
                                        "https://www.instagram.com/sebasti4n.exe/) ❤️", 
                                        color=discord.Colour.random())
        await message.send(embed=sebastian)

    
def setup(bot):
    bot.add_cog(Developers(bot))