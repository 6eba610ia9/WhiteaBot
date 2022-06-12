import discord
from discord.ext import commands

class Afk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    # All you have to add is here:   
    @commands.command()
    async def afk(self, ctx):
        if "(AFK)" in ctx.author.name:
            await ctx.author.edit(nick=f"{ctx.author.name}".replace("(AFK)", ""))
            await ctx.send(f"{ctx.message.author.mention}is not afk anymore")
        
        await ctx.author.edit(nick=f"{ctx.author.name} (AFK)")
        await ctx.send(f"{ctx.message.author.mention}is now afk")

    
def setup(bot):
    bot.add_cog(Afk(bot))