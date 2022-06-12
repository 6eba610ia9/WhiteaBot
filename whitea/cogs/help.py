import discord
from discord.ext import commands

class Help(commands.Cog):
    """Return help about commands and more"""
    def __init__(self, bot):
        self.bot = bot
       
       
    @commands.command()
    async def help(self, message):
        """About Whitea and discord server."""
        embed =  discord.Embed(       
            title="Whitea",
            description="[Open source discord bot.](https://github.com/6eba610ia9/WhiteaBot)",
            color=0xe8e9f0)
        
        embed.set_thumbnail(url="https://raw.githubusercontent.com/6eba610ia9/WhiteaBot/master/assets/whitea.jpg")
        embed.add_field(name="-capybara",
                        value="Generate a random capybara image.",
                        inline=True)
        
        embed.add_field(name="-neko (id)",
                        value="Generate images with specifyed neko id.",
                        inline=True)
        
        embed.set_footer(
            text="Whitea bot.",
            icon_url="https://raw.githubusercontent.com/6eba610ia9/WhiteaBot/master/assets/whitea_rounded.png")
            
        await message.send(embed = embed)
        
def setup(bot):
    bot.add_cog(Help(bot))
    
