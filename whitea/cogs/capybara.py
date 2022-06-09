import requests 
import discord 

class Capybara():
    def __init__(self):
        self.url = 'https://unsplash.com/ngetty/v3/search/images/creative/by-image?image_url=https%3A%2F%2Fs3.us-west-2.amazonaws.com%2Fimages.unsplash.com%2Fsmall%2Fphoto-1525434280327-e525e03f17ef&fields=display_set%2Creferral_destinations%2Ctitle&page_size=200'
        
    def capybara_api(self):
        request = requests.get(self.url)
        api = request.json()
        return api
    
    def query_capybara(self):
        api = self.capybara_api()
        images = api['images']
        results_count = len(images)
        
        import random
        random_url = random.randint(1, results_count)
        
        capybara_image = images[random_url]['display_sizes'][4]['uri']
        capybara_title = images[random_url]['title']
        return capybara_image, capybara_title
    
    
    def capybara(self, ctx):
        url = self.query_capybara()
        embed = discord.Embed(color = 0xf7f1e3,
                              title = f"<:capybara:983651457549086741> {url[1]}")
        embed.set_image(url = url[0])
        return ctx.send(embed=embed)
