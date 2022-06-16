import requests, re
from bs4 import BeautifulSoup
import json
from datetime import datetime

class Hentai():
    """Return images, title and descriptions from hanimes"""
    def __init__(self):
        """ Initialize Class"""
        
        
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
            return regex
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
        return api
                        
    def hentai(self, id):
            api = self.hentai_api(id=id)

            num_pages = api["num_pages"]
            media_id = api["media_id"]
            print(num_pages)
            print(media_id)

print(Hentai().hentai_api(id=174234))
                
                
