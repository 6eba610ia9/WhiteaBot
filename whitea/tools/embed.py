import discord


def newembed(title = "",
             colour=0x428DFF,
             description= ""
             ):
    
    em = discord.Embed(colour=colour, 
                       title=title,
                       description=description
                       )
    em.set_author(
        icon_url="https://raw.githubusercontent.com/6eba610ia9/WhiteaBot/master/whitea/assets/whitea_rounded.png",
        name="Whitea",
        url="https://github.com/6eba610ia9/WhiteaBot"
    )
    return em

