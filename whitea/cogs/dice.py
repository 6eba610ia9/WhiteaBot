import random 
import os 
import asyncio

import discord
from discord.ext import commands


class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
         
    @commands.Cog.listener("on_message")
    async def dice(self, message):
        if message.author.bot:
            return

        if message.content.startswith("🎲"):

            dice_nr = random.randint(1, 6)
            gif = f"https://raw.githubusercontent.com/6eba610ia9/WhiteaBot/master/assets/dice_gif/{dice_nr}.gif"
            
            embed = discord.Embed(color=discord.Color.random())
            embed.set_thumbnail(url=gif)

            await message.channel.send(embed=embed)
            


    
def setup(bot):
    bot.add_cog(Dice(bot))