import discord
from discord.ext import commands
import requests, re
from bs4 import BeautifulSoup
import json
from datetime import datetime


class Hentai:
    
    def __init__(self, bot, id):
        """ Initialize Class"""
        self.id = id
        self.bot = bot

        
    def hentai_img(self, media_id, page=1):
        url = f"https://t.dogehls.xyz/galleries/{media_id}/{page}.jpg"
        return url

    def hentai_api(self):
        id = self.id
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
    
    
    def thubnail_embed(self):
        
        api = self.hentai_api()
        title = api["title"]["pretty"]
        title_japanese = api["title"]["japanese"]
        
        media_id = api["media_id"]
        num_pages = api["num_pages"]
        # Upload date formated
        upload_epoch = api["upload_date"]
        upload_date = datetime.fromtimestamp(upload_epoch)
        upload_date.strftime("%m/%d/%Y, %H:%M:%S")
        
        thubnail = self.hentai_img(media_id=media_id)
        
        embed = discord.Embed(
            title = title,
            description = f"[{title_japanese}](https://nhentai.to/g/{self.id})",
            color = 0x89CFF0
        )
        
        embed.set_thumbnail(url=thubnail)
        embed.add_field(name="Num pages", value=num_pages, inline=False)
        embed.add_field(name="Uploaded at", value=upload_date, inline=False)
        
        for tag in api["tags"]:
            embed.add_field(name=tag["type"], value=tag["name"], inline=True)
        
        return embed
                        

    async def hentai(self, ctx):
            api = self.hentai_api()
            num_pages = api["num_pages"]
            media_id = api["media_id"]

                
            for page in range (1, num_pages):
                image = self.hentai_img(media_id=media_id, page=page)
                embed = self.thubnail_embed()

                if page == 1:
                    img = ctx.send(embed=embed)
                    return img
                else: 
                    img.edit(content=image)

                    img.add_reaction("⬅️")
                    img.add_reaction("➡️")
                
                valid_reactions = ["⬅️", "➡️"]

                def check(reaction, user):
                    return user == ctx.author and str(reaction.emoji) in valid_reactions
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                if str(reaction.emoji) == "➡️":
                    continue
                
                
                
