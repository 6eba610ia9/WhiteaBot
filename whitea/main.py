import discord
import random
from discord.ext import commands
from variables.token import TOKEN
from variables.prefix import PREFIX
from bs4 import BeautifulSoup
import requests, re
from requests import get
import json
from tools import messages, embed
from cogs.hentai import Hentai
from cogs.capybara import Capybara

activity = discord.Activity(type=discord.ActivityType.watching, name="sexy capybara")

bot = commands.Bot(command_prefix=PREFIX, 
                   help_command=None, 
                   status=discord.Status.idle, 
                   activity=activity)





bot.run(TOKEN)
