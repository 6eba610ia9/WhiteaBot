import discord


def newembed(text, c=0x428DFF):
    em = discord.Embed(colour=c)
    em.set_footer(text=text,
                  icon_url="https://raw.githubusercontent.com/6eba610ia9/WhiteaBot/master/whitea/assets/whitea_rounded.png")

    return em

