import requests
import discord
from discord.ext import commands



class Neko(commands.Cog):
    """Random neko image generator"""
    def __init__(self, bot):
        self.bot = bot
        
        
    def newembed(self, text):
        em = discord.Embed(colour=discord.Colour.random())
        em.set_footer(text=f"Here's your {text}",
                    icon_url="https://raw.githubusercontent.com/6eba610ia9/WhiteaBot/master/assets/whitea_rounded.png")

        return em
    
    def error(self, e="executing command"):
        return discord.Embed(title=f"⚠ Unknown error occurred while {e}!",
                         description="Please report to [Whitea.py](https://github.com/6eba610ia9/WhiteaBot)!",
                         color=0xFF0000)


    def neko_api(self, message, x):
        try:
            req = requests.get(f'https://nekos.life/api/v2/img/{x}')
            if req.status_code != 200:
                print("Could not get a neko")
            apijson = req.json()
            url = apijson["url"]
            em = self.newembed(text=x).set_image(url=url)
            return em
        except:
            return self.error(f"obtaining image ({req.status_code})")

    @commands.command()
    async def neko(self, message):
        await message.send(embed=self.neko_api(message, "neko"))

    @commands.command()
    async def waifu(self, message):
        await message.send(embed=self.neko_api(message, "waifu"))

    @commands.command()
    async def avatar(self, message):
        await message.send(embed=self.neko_api(message, "avatar"))

    @commands.command()
    async def wallpaper(self, message):
        await message.send(embed=self.neko_api(message, "wallpaper"))

    @commands.command()
    async def tickle(self, message):
        await message.send(embed=self.neko_api(message, "tickle"))

    @commands.command()
    async def poke(self, message):
        await message.send(embed=self.neko_api(message, "poke"))

    @commands.command()
    async def kiss(self, message):
        await message.send(embed=self.neko_api(message, "kiss"))

    @commands.command(aliases=['8ball'])
    async def eightball(self, message):
        await message.send(embed=self.neko_api(message, "8ball"))

    @commands.command()
    async def lizard(self, message):
        await message.send(embed=self.neko_api(message, "lizard"))

    @commands.command()
    async def slap(self, message):
        await message.send(embed=self.neko_api(message, "slap"))

    @commands.command()
    async def cuddle(self, message):
        await message.send(embed=self.neko_api(message, "cuddle"))

    @commands.command()
    async def goose(self, message):
        await message.send(embed=self.neko_api(message, "goose"))

    @commands.command()
    async def fox_girl(self, message):
        await message.send(embed=self.neko_api(message, "fox_girl"))

    @commands.command()
    async def baka(self, message):
        await message.send(embed=self.neko_api(message, "baka"))
        
        
def setup(bot):
    """ Setup Neko Module"""
    bot.add_cog(Neko(bot))