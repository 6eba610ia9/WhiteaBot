import discord
from discord.ext import commands
from variables.token import TOKEN
from variables.prefix import PREFIX
import os

activity = discord.Activity(type=discord.ActivityType.watching, name="sexy capybara")

bot = commands.Bot(command_prefix=PREFIX, 
                   help_command=None, 
                   status=discord.Status.idle, 
                   activity=activity)





@bot.command()

async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

    
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./whitea/cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')





bot.run(TOKEN)
