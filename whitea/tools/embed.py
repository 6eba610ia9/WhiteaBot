
import discord



def newembed(c=0x428DFF):
    em = discord.Embed(colour=c)
    em.set_footer(text="Copyright free",
                  icon_url="")

    return em