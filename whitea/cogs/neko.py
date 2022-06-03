import discord
from discord.ext import commands
import requests, re
from bs4 import BeautifulSoup




def neko_image(id, page):
    url = f"https://t.dogehls.xyz/galleries/{id}/{page}.jpg"
    return url


async def neko(context, id):
    url = f"https://nhentai.to/g/{id}/1"
    request = requests.get(url)

    if request.status_code == 200:
        html = request.text
        soup = BeautifulSoup(html, "html.parser")
        script = soup.find_all("script")[4].text
        regex = re.search(r"gallery: {.*?},(\s+)(\w)", script, re.DOTALL).group(0)[9:-20]
        json = json.loads(regex + "}")
        
        title = json["title"]["english"]
        media_id = title = json["media_id"]
        num_pages = json["num_pages"]
        print(json)
        for page in range (1, num_pages):
            image = neko_image(id=media_id, page=page)
            await context.send(image)
            
    else:
        await context.send("Neko not found...")
        

