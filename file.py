import requests 

def ig(username):
    user = username.replace('@', "")
    
    url = f'https://www.instagram.com/{user}/?__a=1&__d=dis'
    agent = {"User-Agent":"Mozilla/5.0"}
    request = requests.get(url, headers=agent)
    json = request.json()
    followers = json
    print(followers)
ig("justzetu")