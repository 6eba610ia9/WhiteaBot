import discord 

def WIP():
    """Work In Progress"""
    return discord.Embed(title="⏲ This feature is work in progress!",
                        description="Please stay tuned to our latest updates [here]("
                                     "https://github.com/6eba610ia9/WhiteaBot)!", 
                        color=0x89CFF0
    )
def about():
    """About Whitea and discord server."""
    return discord.Embed(
        type="rich",             
        title="[🍵 Whitea]('https://github.com/6eba610ia9/WhiteaBot')",
        description="This is first open source discord bot!",
        color=0xe8e9f0,
        footer="Copyright free",        
        thubnail="https://i.imgflip.com/3ybq17.jpg"         
    )