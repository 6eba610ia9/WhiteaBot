import discord
from discord.ext import commands

class Developers(commands.Cog):
    """About bot developers"""
    def __init__(self, bot):
        self.bot = bot
       
    @commands.command()
    async def developers(self, message):
        """Zet"""
        embed =  discord.Embed(title="<:b_file:984970328444923914>  **Developers:**",
                                        color= 0x800080)
        
        embed.add_field(name="<:b_Ide:985866239538778153> Zet",
                        value="\u200b \u200b <:3214instagram:986599640524812308>  [**Justzetu**](https://www.instagram.com/justzetu/)\n"
                            "\u200b \u200b <:d_github:986605201853149275>  [**JustZet**](https://github.com/justzet) "
                        )
        embed.add_field(
                          name= " <:w_RG:985866241338130472> Seby",
                            value= "\u200b \u200b <:3214instagram:986599640524812308>  [**Sebasti4n.exe**](https://www.instagram.com/sebasti4n.exe/) \n"
                            "\u200b \u200b <:d_github:986605201853149275> [**6eba610ia9**](https://github.com/6eba610ia9)"
        )
        await message.send(embed=embed)
        
        
    @commands.command()
    async def zet(self, message):
        """Zet"""
        zet =  discord.Embed(title="Support Developer ❤️",
                            description="Follow on  [Insta]("
                                        "https://www.instagram.com/justzetu/) 👀", 
                                        color=discord.Colour.random())
        await message.send(embed=zet)

    @commands.command()
    async def sebastian(self, message):
        """Sebastian"""
        sebastian =  discord.Embed(title="Support Developer ❤️",
                            description="Follow on [Insta]("
                                        "https://www.instagram.com/sebasti4n.exe/) ❤️", 
                                        color=discord.Colour.random())
        await message.send(embed=sebastian)

    
def setup(bot):
    bot.add_cog(Developers(bot))