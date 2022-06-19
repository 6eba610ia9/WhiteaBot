import discord
from discord.ext import commands
import random

class BassicCommands(commands.Cog):
    """Return a random procent of lgbt rate"""
    def __init__(self, bot):
        self.bot = bot
       
    # All you have to add is here:   
    @commands.command()
    
    async def gay(self, message, member=None):
        procents = random.randint(0, 100)
        # if author don't tag anyone
        if member is None:
            embed = discord.Embed(colour=discord.Colour.random(), 
                        description=f"You are {procents}% gay")
            message = await message.send(embed = embed)
        # if author send command with member ping
        else:
            embed = discord.Embed(colour=discord.Colour.random(), 
                        description=f"{member} is {procents}% gay lol")
            message = await message.send(embed = embed)
            
            
    @commands.command()
    async def afk(self, ctx):
        """Move you in afk mode"""
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
    bot.add_cog(BassicCommands(bot))