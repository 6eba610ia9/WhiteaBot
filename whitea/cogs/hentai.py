from discord.ext import commands
from NHentai import NHentai
import discord



class Hentai(commands.Cog):
    """Return images, title and descriptions from hanimes"""
    def __init__(self, bot):
        """ Initialize Class"""
        self.bot = bot
        self.nhentai = NHentai()

    
    def embed(self, id):
        hentai = self.nhentai.search(query=id, page=1)
        
        embed = discord.Embed(
            title=hentai.title.pretty,
            
            color = discord.Colour.random()
        )
        embed.add_field(name="<:b_file:984970328444923914> Num pages:", value=hentai.total_pages, inline=False)
        embed.add_field(name="<:w_heart_hand:985813367908356157> Favorites:", value=hentai.total_favorites, inline=False)
        embed.add_field(name=":clock: Uploaded at:", value=hentai.upload_at, inline=False)
        embed.set_thumbnail(url=hentai.cover.src)
        
        tags = hentai.tags
        
        for tag in tags:
            embed.add_field(name=tag.type, 
                            value=tag.name, 
                            inline=True)
        
        return embed
                        
    @commands.command()
    async def hentai(self, message, id):
        
        await message.send(embed=self.embed(id))
        
                
def setup(bot):
    bot.add_cog(Hentai(bot))
                
                
                
