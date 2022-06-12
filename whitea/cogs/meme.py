import discord
from discord.ext import commands
import json
from requests import get

class Template(commands.Cog):
    """Random meme generator"""
    def __init__(self, bot):
        self.bot = bot
       
    
    @commands.command()
    async def meme(self, message):
        content = get("https://meme-api.herokuapp.com/gimme").text
        data = json.loads(content)
        title = data['title']
        url = data['url']
        embed = discord.Embed(title=title, 
                             Color = discord.Color.random())
        embed.set_image(url=url)
        
        await message.reply(embed=embed)

def setup(bot):
    bot.add_cog(Template(bot))