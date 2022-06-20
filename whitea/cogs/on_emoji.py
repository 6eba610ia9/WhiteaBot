import random 
import os 
import asyncio

import requests
import discord
from discord.ext import commands


class OnEmoji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    def error(self, e="executing command"):
        return discord.Embed(title=f"⚠ Unknown error occurred while {e}!",
                         description="Please report to [Whitea.py](https://github.com/6eba610ia9/WhiteaBot)!",
                         color=0xFF0000)
        
    
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
            
    async def coin(self, message):
        if message.author.bot:
            return

        if message.content.startswith("🪙"):

            coin_nr = random.randint(1, 8)
            gif = f"https://raw.githubusercontent.com/6eba610ia9/WhiteaBot/master/assets/heads%20and%20tails/{coin_nr}.gif"
            
            embed = discord.Embed(color=discord.Color.random())
            embed.set_thumbnail(url=gif)

            await message.channel.send(embed=embed)
            
    def eightball(self, message):
        try:
            req = requests.get(f'https://nekos.life/api/v2/img/8ball')
            apijson = req.json()
            url = apijson["url"]
            embed = discord.Embed(colour=discord.Colour.random())
            embed.set_image(url=url)
            return embed
        except:
            return self.error(f"obtaining image ({req.status_code})")   
             
    @commands.Cog.listener("on_message")
    async def ball8(self, message):
        if message.author.bot:
            return

        if message.content.startswith("🎱"):
            await message.channel.send(embed=self.eightball(message))


    
def setup(bot):
    bot.add_cog(OnEmoji(bot))