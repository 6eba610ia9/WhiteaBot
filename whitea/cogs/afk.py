import discord
from discord.ext import commands

class Afk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    # All you have to add is here:   
    @commands.command()
    async def afk(self, ctx):
        
        # if user have nickname in guild
        if ctx.author.nick:
            
            # if user is already afk
            if "(AFK)" in ctx.author.nick:
                
                await ctx.author.edit(nick=f"{ctx.author.nick}".replace("(AFK)", ""))
                await ctx.send(f"{ctx.message.author.mention} is not afk anymore")
                
            # if user is not afk
            elif ctx.author.nick:
                
                await ctx.author.edit(nick=f"{ctx.author.nick} (AFK)")
                await ctx.send(f"{ctx.message.author.mention} is now afk")
                
        # if user don't have nickname in guild
        elif ctx.author.name:
            
            await ctx.author.edit(nick=f"{ctx.author.name} (AFK)")
            await ctx.send(f"{ctx.message.author.mention} is now afk")
            
        
def setup(bot):
    bot.add_cog(Afk(bot))