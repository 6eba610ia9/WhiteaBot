
import discord
import requests


def newembed(text, c=0x428DFF):
    em = discord.Embed(colour=c)
    em.set_footer(text=text,
                  icon_url="https://github.com/6eba610ia9/WhiteaBot/blob/master/whitea/assets/whitea_rounded.png?raw=true")

    return em

def capybara(ctx):
    url = 'https://unsplash.com/ngetty/v3/search/images/creative/by-image?image_url=https%3A%2F%2Fs3.us-west-2.amazonaws.com%2Fimages.unsplash.com%2Fsmall%2Fphoto-1525434280327-e525e03f17ef&fields=display_set%2Creferral_destinations%2Ctitle&page_size=200'
    api = requests.get(url).json()
    
    results_count = len(api['images'])
    
    import random
    random = random.randint(1, results_count)
    capybara = api['images'][random]['display_sizes'][4]['uri']
    
    embed = discord.Embed(color = 0xf7f1e3)
    embed.set_image(url = capybara)
    return ctx.send(embed=embed)