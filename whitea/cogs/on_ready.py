import discord
from discord.ext import commands

class OnReady(commands.Cog):
    """On ready bot default message"""
    def __init__(self, bot):
        self.bot = bot
       
       
    @commands.Cog.listener()
    async def on_ready(self):
        print(
            
            f'{self.bot.user} is connected!\n'
            f'Prefix : {self.bot.command_prefix}'
        )

    
def setup(bot):
    bot.add_cog(OnReady(bot))