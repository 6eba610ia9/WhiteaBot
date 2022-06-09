import requests
import discord
from discord.ext import commands



class Neko():
    def __init__(self, bot):
        self.bot = bot
        
        
    def newembed(text, c=0x428DFF):
        em = discord.Embed(colour=c)
        em.set_footer(text=text,
                    icon_url="https://raw.githubusercontent.com/6eba610ia9/WhiteaBot/master/whitea/assets/whitea_rounded.png")

        return em
    
    def error(self, e="executing command"):
        return discord.Embed(title=f"⚠ Unknown error occurred while {e}!",
                         description="Please report to [Teapot.py](https://github.com/RedCokeDevelopment/Teapot.py) developers [here](https://github.com/RedCokeDevelopment/Teapot.py/issues)!",
                         color=0xFF0000)


    def neko_api(self, ctx, x):
        try:
            req = requests.get(f'https://nekos.life/api/v2/img/{x}')
            if req.status_code != 200:
                print("Could not get a neko")
            apijson = req.json()
            url = apijson["url"]
            em = self.newembed().set_image(url=url)
            return em
        except:
            return self.error(f"obtaining image ({req.status_code})")

    @commands.command()
    async def neko(self, ctx):
        await ctx.send(embed=self.neko_api(ctx, "neko"))

    @commands.command()
    async def waifu(self, ctx):
        await ctx.send(embed=self.neko_api(ctx, "waifu"))

    @commands.command()
    async def avatar(self, ctx):
        await ctx.send(embed=self.neko_api(ctx, "avatar"))

    @commands.command()
    async def wallpaper(self, ctx):
        await ctx.send(embed=self.neko_api(ctx, "wallpaper"))

    @commands.command()
    async def tickle(self, ctx):
        await ctx.send(embed=self.neko_api(ctx, "tickle"))

    @commands.command()
    async def poke(self, ctx):
        await ctx.send(embed=self.neko_api(ctx, "poke"))

    @commands.command()
    async def kiss(self, ctx):
        await ctx.send(embed=self.neko_api(ctx, "kiss"))

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx):
        await ctx.send(embed=self.neko_api(ctx, "8ball"))

    @commands.command()
    async def lizard(self, ctx):
        await ctx.send(embed=self.neko_api(ctx, "lizard"))

    @commands.command()
    async def slap(self, ctx):
        await ctx.send(embed=self.neko_api(ctx, "slap"))

    @commands.command()
    async def cuddle(self, ctx):
        await ctx.send(embed=self.neko_api(ctx, "cuddle"))

    @commands.command()
    async def goose(self, ctx):
        await ctx.send(embed=self.neko_api(ctx, "goose"))

    @commands.command()
    async def fox_girl(self, ctx):
        await ctx.send(embed=self.neko_api(ctx, "fox_girl"))

    @commands.command()
    async def baka(self, ctx):
        await ctx.send(embed=self.neko_api(ctx, "baka"))
        
        
def setup(bot):
    """ Setup Neko Module"""
    bot.add_cog(Neko(bot))