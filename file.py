import requests 
from bs4 import BeautifulSoup

def instagram(username):
    user = username.replace('@', "")

    url = f'https://www.instagram.com/{user}/?__a=1&__d=dis'
    request = requests.get(url)
    html = BeautifulSoup(request, 'html.parser').find_all("div").text
    json = request.text
    followers = json
    print(html)

instagram('justzetu')