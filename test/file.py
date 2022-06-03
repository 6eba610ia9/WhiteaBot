import requests 
from bs4 import BeautifulSoup

def instagram(username):
    agent = {"User-Agent":"Mozilla/5.0"}
    user = username.replace('@', "")

    url = f'https://www.instagram.com/{user}/?__a=1&__d=dis'
    request = requests.get(url, headers=agent).json()

    print(request)

instagram('justzetu')