import discord
from discord.ext import commands
import requests, re
from bs4 import BeautifulSoup
import json


class Neko():
    
    def __init__(self, bot):
        """ Initialize Cat Class"""

        self.bot = bot
        
        
    def neko_image(self, id, page):
        url = f"https://t.dogehls.xyz/galleries/{id}/{page}.jpg"
        return url

    def neko_api(self, id):
        url = f"https://nhentai.to/g/{id}/1"
        request = requests.get(url)
        if request.status_code == 200:
            html = request.text
            soup = BeautifulSoup(html, "html.parser")
            script = soup.find_all("script")[4].text
            regex = re.search(r"gallery: {.*?},(\s+)(\w)", script, re.DOTALL).group(0)[9:-20]
            api = json.loads(regex + "}")
            return api
            
        else:
            return "404"
    
    
    def types(api):
        len_type = len(api["tags"])
        all_tags = {}
        for count in range(len_type):
            type = api["tags"][count]["type"]
            name = api["tags"][count]["name"]
            tags = {f"{type}" : f"{name}"}
            all_tags.update(tags)
        return(all_tags)
    
    
    async def neko_data(self, ctx, id):
            api = self.neko_api(id)
            title = api["title"]["english"]
            media_id = api["media_id"]
            num_pages = api["num_pages"]
            

            
            for page in range (1, num_pages):
                image = self.neko_image(id=media_id, page=page)
                            
                description = discord.Embed(title=title,
                                            description=image,
                                            color=0x89CFF0)
                
                if page == 1:
                    img = ctx.send(embed=description)
                    return img
                else: 
                    img.edit(content=image)

                    await img.add_reaction("⬅️")
                    await img.add_reaction("➡️")
                
                valid_reactions = ["⬅️", "➡️"]

                def check(reaction, user):
                    return user == ctx.author and str(reaction.emoji) in valid_reactions
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                if str(reaction.emoji) == "➡️":
                    continue
                