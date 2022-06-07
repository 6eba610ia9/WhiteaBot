import discord
from discord.ext import commands
from variables.token import TOKEN
from variables.prefix import PREFIX
from bs4 import BeautifulSoup
import requests, re
import json
from tools import messages, embed
from cogs.neko import Neko
from cogs.capybara import Capybara
from tools import messages 

bot = commands.Bot(command_prefix=PREFIX, help_command=None)

#mesaj logare bot - NU EDITA NIMIC!
@bot.event
async def on_ready():
    print(
        
        f'{bot.user} is connected!\n'
        f'Prefix : {bot.command_prefix}'
    )
@bot.command()
async def about(ctx):
    await ctx.send(embed= messages.about())

@bot.command(aliases=['news', 'github', 'source', 'features', 'info'])
async def _info(ctx):
    await ctx.send(embed=messages.WIP())

@bot.command()
async def help(ctx):
    await ctx.send(embed=embed.newembed("This will be the help message"))

@bot.command()
async def zet(ctx):
    """Zet"""
    zet =  discord.Embed(title="Zet are cel mai mare dragon 🐉",
                         description="Click here  [here]("
                                     "https://i.imgflip.com/3ybq17.jpg) to see 👀", color=0x89CFF0)
    await ctx.send(embed=zet)


def hentai_image(id, page):
    url = f"https://t.dogehls.xyz/galleries/{id}/{page}.jpg"
    return url

@bot.command(aliases=['hentai', 'hanime', 'neko'])
async def _neko(ctx, id):
    url = f"https://nhentai.to/g/{id}/1"
    request = requests.get(url)

    if request.status_code == 200:
        html = request.text
        soup = BeautifulSoup(html, "html.parser")
        script = soup.find_all("script")[4].text
        regex = re.search(r"gallery: {.*?},(\s+)(\w)", script, re.DOTALL).group(0)[9:-20]
        api = json.loads(regex + "}")
        
        title = api["title"]["english"]
        media_id = api["media_id"]
        num_pages = api["num_pages"]
        
        def types(count):
            
            type = api["tags"][count]["type"]
            name = api["tags"][count]["name"]
            
            return type, name
        
        for page in range (1, num_pages):
            image = hentai_image(id=media_id, page=page)
            
            embed = discord.Embed(title=title,
                            color=0x89CFF0)
            embed.set_thumbnail(url=image)
            embed.add_field(name="Num pages:", value=num_pages, inline=True)
            
            for tag in api["tags"]:
                embed.add_field(name=tag["type"], value=tag["name"], inline=True)
                
                
            if page == 1:
                img = await ctx.send(embed=embed)
            else: 
                await img.edit(content=image)
                await img.add_reaction("⬅️")
                await img.add_reaction("➡️")
            
            valid_reactions = ["⬅️", "➡️"]

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in valid_reactions
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)

            if str(reaction.emoji) == "➡️":
                continue
            
    else:
        await ctx.send("Neko not found...")


@bot.command(aliases = ["capybara"])
async def _capybara(ctx):
    """
    Return random capybara images
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    
    await Capybara().capybara(ctx=ctx)
    

@bot.command()
async def nekko(ctx, id):
    hentai = Neko(bot=bot).neko_data(ctx=ctx, id=id)
    await ctx.send(hentai)
    
bot.run(TOKEN)
