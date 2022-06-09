from email import generator
import discord
import random
from discord.ext import commands
from variables.token import TOKEN
from variables.prefix import PREFIX
from bs4 import BeautifulSoup
import requests, re
import json
from tools import messages, embed
from cogs.hentai import Hentai
from cogs.capybara import Capybara
from tools import messages

activity = discord.Activity(type=discord.ActivityType.watching, name="sexy capybara")

bot = commands.Bot(command_prefix=PREFIX, 
                   help_command=None, 
                   status=discord.Status.idle, 
                   activity=activity)


#mesaj logare bot - NU EDITA NIMIC!
@bot.event
async def on_ready():
    print(
        
        f'{bot.user} is connected!\n'
        f'Prefix : {bot.command_prefix}'
    )
    
    
# @bot.event
# async def on_message(message):
#     print(f'Guild: {message.guild.name}, User: {message.author}, Message: {message.content}')
#     if message.author == bot.user:
#         return
    

@bot.command()
async def help(ctx):
    await ctx.send(embed= messages.about())

@bot.command(aliases=['news', 'github', 'source', 'features', 'info'])
async def _info(ctx):
    await ctx.send(embed=messages.WIP())


@bot.command()
async def zet(ctx):
    """Zet"""
    zet =  discord.Embed(title="Zet are cel mai mare dragon 🐉",
                         description="Click here  [here]("
                                     "https://i.imgflip.com/3ybq17.jpg) to see 👀", color=0x89CFF0)
    await ctx.send(embed=zet)


@bot.command(aliases=['hentai', 'hanime'])
async def _hentai(ctx, id):
    neko = await Hentai(bot=bot, id=id).hentai(ctx=ctx)
    await neko
    

@bot.command(aliases = ["capybara"])
async def _capybara(ctx):
    """
    Return random capybara images
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    
    await Capybara().capybara(ctx=ctx)

@bot.command()
async def neko(ctx):
    request = requests.get("https://nekos.life/api/v2/img/neko")
    api = request.json()
    neko = api["url"]
    await ctx.send(neko)
    
@bot.command()
async def gay(ctx):
    procents = random.randint(0,100)
    await ctx.send(embed=embed.newembed(f"{ctx.author} este {procents}% gay ❤️" ))

@bot.command()
async def run(ctx, params):
    await ctx.send(params)


<<<<<<< HEAD

=======
        
>>>>>>> 1e2856bf4eeca48cfd7ee86cc30b81f3889d5a84
bot.run(TOKEN)
