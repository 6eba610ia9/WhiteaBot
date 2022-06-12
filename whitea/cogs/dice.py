import random 
import os 

import discord
from discord.ext import commands


class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
         
    @commands.Cog.listener("on_message")
    async def dice(self, message):
        if message.author.bot:
            return
        
        if message.content == "🎲" or ":game_die:":
            dice_nr = random.randint(1, 6)
            url = f"https://raw.githubusercontent.com/6eba610ia9/WhiteaBot/master/whitea/cogs/dice/{dice_nr}.gif"
            
            embed = discord.Embed(color=discord.Color.random())
            embed.set_image(url=url)
            
                
            await message.reply(embed=embed)


    
def setup(bot):
    bot.add_cog(Dice(bot))


