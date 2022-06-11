import os
import random 

from PIL import Image
import discord
from discord.ext import commands


class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
         
    @commands.command()
    async def dice(self, ctx):
        imgList = os.listdir("C:/Users/Zet/Documents/bot/whitea/cogs/dice") # Creates a list of filenames from your folder

        imgString = random.choice(imgList) # Selects a random element from the list

        path = "C:/Users/Zet/Documents/bot/whitea/cogs/dice/" + imgString # Creates a string for the path to the file

        await ctx.send_file(path) # Sends the image in the channel the command was used


    
def setup(bot):
    bot.add_cog(Dice(bot))


