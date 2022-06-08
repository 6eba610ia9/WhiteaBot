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


@bot.command(aliases=['hentai', 'hanime', 'neko'])
async def _neko(ctx, id):
    neko = await Neko(bot=bot, id=id).neko_data(ctx=ctx)
    await neko
    

@bot.command(aliases = ["capybara"])
async def _capybara(ctx):
    """
    Return random capybara images
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    
    await Capybara().capybara(ctx=ctx)


@bot.command()
async def gay(ctx):
    procents = random.randint(0,100)
    await ctx.send(embed=embed.newembed(f"{ctx.author} is {procents}% gay" ))

@bot.command()
async def run(ctx, params):
    await ctx.send(params)


        
bot.run(TOKEN)
