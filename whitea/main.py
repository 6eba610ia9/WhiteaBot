import discord
from discord.ext import commands
from variables.token import TOKEN
from variables.prefix import PREFIX
from bs4 import BeautifulSoup
import requests, re
import json
from time import sleep


# client = discord.Client()
client = commands.Bot(command_prefix=PREFIX)

#mesaj logare bot - NU EDITA NIMIC!
@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds)
    print(
        f'{client.user} is connected\n'
    )


# @client.command(aliases=['instagram', 'ig', 'insta'])
# async def _instagram(ctx, username):
#     user = username.replace('@', "")

#     url = f'https://www.instagram.com/{user}/?__a=1&__d=dis'
#     request = requests.get(url)
#     json = request.json()
#     followers = json
#     print(followers)
#     # await ctx.send(json_data)


def hentai_image(id, page):
    url = f"https://t.dogehls.xyz/galleries/{id}/{page}.jpg"
    return url

@client.command(aliases=['hentai', 'hanime'])
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

        for page in range (1, num_pages):
            image = hentai_image(id=media_id, page=page)
            img = await ctx.send(image)
            await img.add_reaction("⬅️")
            await img.add_reaction("➡️")
            
            valid_reactions = ["⬅️", "➡️"]

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in valid_reactions
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)

            if str(reaction.emoji) == "➡️":
                continue
            
    else:
        await ctx.send("Neko not found...")



client.run(TOKEN)
