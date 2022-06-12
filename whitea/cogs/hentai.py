import discord
import requests, re
from bs4 import BeautifulSoup
import json
from datetime import datetime
from discord.ext import commands


class Hentai(commands.Cog):
    """Return images, title and descriptions from hanimes"""
    def __init__(self, bot):
        """ Initialize Class"""
        self.bot = bot

        
    def hentai_img(self, media_id, page=1):
        url = f"https://t.dogehls.xyz/galleries/{media_id}/{page}.jpg"
        return url

    def hentai_api(self, id):
        url = f"https://nhentai.to/g/{id}/1"
        request = requests.get(url)
        if request.status_code == 200:
            html = request.text
            soup = BeautifulSoup(html, "html.parser")
            script = soup.find_all("script")[5].text
            regex = re.search(r"gallery: {.*?},(\s+)(\w)", script, re.DOTALL)
            regex.group(0)[9:-20]
            api = json.loads(regex + "}")
            return api
            
        else:
            return "404"
    
    
    def embed(self, id):
        
        api = self.hentai_api(id=id)
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
            description = f"[{title_japanese}](https://nhentai.to/g/{id})",
            color = discord.Colour.random()
        )
        embed.set_thumbnail(url=thubnail)
        embed.add_field(name="Num pages", value=num_pages, inline=False)
        embed.add_field(name='----------------------------------------------------------------------------', value = "**----------------------------------------------------------------------------**", inline=False)
        embed.add_field(name="Uploaded at", value=upload_date, inline=False)
        
        for tag in api["tags"]:
            embed.add_field(name=tag["type"], value=tag["name"], inline=True)
        
        return embed
                        
    @commands.command()
    async def hentai(self, message, id):
            api = self.hentai_api(id=id)

            num_pages = api["num_pages"]
            media_id = api["media_id"]

                
            for page in range (1, num_pages):
                image = self.hentai_img(media_id=media_id, page=page)
                embed = self.embed(id=id)
                if page == 1:
                    img = message.send(embed=embed)
                    await img
                else: 
                    await img.edit(content=image)

                    await img.add_reaction("⬅️")
                    await img.add_reaction("➡️")
                
                valid_reactions = ["⬅️", "➡️"]

                def check(reaction, user):
                    return user == message.author and str(reaction.emoji) in valid_reactions
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                if str(reaction.emoji) == "➡️":
                    continue
                
def setup(bot):
    bot.add_cog(Hentai(bot))
                
                
                
