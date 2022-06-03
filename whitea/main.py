import discord
from discord.ext import commands
from variables.token import TOKEN
from variables.prefix import PREFIX
from bs4 import BeautifulSoup
import requests, re
import json
from time import sleep
from variables import PREFIX, TOKEN
from cogs.neko import neko
from tools.embed import newembed

client = commands.Bot(command_prefix=PREFIX)

@client.event
async def on_ready():
    print(f'{client.user} is connected\n')

# @client.command(aliases=['neko', 'hentai', 'hanime'])
# async def _neko(ctx, id):
#     await neko(context=ctx, id=id)



client.run(TOKEN)
 