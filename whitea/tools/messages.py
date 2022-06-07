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
    embed =  discord.Embed(       
        title="Whitea",
        description="[Open source discord bot.](https://github.com/6eba610ia9/WhiteaBot)",
        color=0xe8e9f0,     
    )
    embed.set_thumbnail(url="https://raw.githubusercontent.com/6eba610ia9/WhiteaBot/master/whitea/assets/whitea.jpg")
    embed.add_field(name="-capybara",
                    value="Generate a random capybara image.",
                    inline=True
                    )
    embed.add_field(name="-neko (id)",
                    value="Generate images with specifyed neko id.",
                    inline=True
                    )
    embed.set_footer(
        text="Whitea bot.",
        icon_url="https://raw.githubusercontent.com/6eba610ia9/WhiteaBot/master/whitea/assets/whitea_rounded.png"
    )
    return embed