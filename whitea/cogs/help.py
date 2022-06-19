import discord
from discord.ext import commands

class Help(commands.Cog):
    """Return help about commands and more"""
    def __init__(self, bot):
        self.bot = bot
        
       
       
       
    @commands.command()
    async def help(self, message):
        """About Whitea and discord server."""
        
        white_spaces = "\u200b \u200b \u200b \u200b \u200b \u200b \u200b \u200b \u200b"
        
        def commands():
            emojis = ["Neko", "Waifu"]
            commands = ["-neko", "-waifu"]
            description = ["return neko image", "return waifu image"]
            
            for element in emojis, commands, description:
                string = f"{white_spaces} {element}"
                print(string)
            
        embed =  discord.Embed(       
            title="Whitea",
            color=discord.Color.random())
        
        embed.set_thumbnail(url="https://raw.githubusercontent.com/6eba610ia9/WhiteaBot/master/assets/whitea.jpg")
        embed.add_field(name="<:p_milk:985813348039942214> Neko:",
                        value=
                        f"{white_spaces}<:p_coffies:985813365739892756> **-neko:** Shows a neko image \n"
                        f"{white_spaces}<:o_uwu:985844529582202900> **-waifu:** Waifu image \n"
                        f"{white_spaces}<:o_juice_cup:985813346328649739> **-avatar:** Neko avatar \n"
                        f"{white_spaces}<:w_cloud:985813369623838751> **-wallpaper:** Neko wallpaper \n"
                        f"{white_spaces}<:w_heart_hand:985813367908356157> **-tickle:** Tickle gif \n"
                        f"{white_spaces}<:o_kiss:985844569604251678> **-kiss:** Kiss gif \n"
                        f"{white_spaces}<:y_slap:985844603481645087> **-slap:** Slap gif \n"
                        f"{white_spaces}<:o_cuddling:985844572192120872> **-cuddle:** Hug gif \n"
                        f"{white_spaces}<:w_baka:985844527594078268> **-baka:** Baka image  \n"
                        f"{white_spaces}<:o_foxgirl:985846658719969341> **-fox_girl:** Foxy neko girl \n",
                        inline=False)
        
        embed.add_field(name="<:m_elixir:984970764564434994> Info:",
                        value=f"{white_spaces}<:b_Ide:985866239538778153>  **-developers:** Shows devs info \n" 
                              f"{white_spaces}<a:w_papper:985813363932168233>  **-source:** Source code \n"
                              f"{white_spaces}<:p_coffies:985813365739892756>  **-support:** You can add one up vote [here](https://top.gg/bot/982162391318036520/vote). \n "
                              f"{white_spaces}{white_spaces}{white_spaces}{white_spaces}  it helps us a lot and its free :) \n",
                        inline=False)
        
        embed.add_field(name="<:c_engrenagem:985866236774711296> Config:",
                        value=f"{white_spaces}<a:y_juice:985813363055534110> **-afk:** It adds you to afk mode and takes you out if you're in \n",
                        inline=False)
        
                
        embed.add_field(name="<a:g_dia:985813353844862996> Utility:",
                        value=f"{white_spaces} You can only send 🎲 in chat and the bot will reply with a dice gif. \n",
                        inline=False)
        
        
        embed.set_footer(
            text="Whitea bot.",
            icon_url="https://raw.githubusercontent.com/6eba610ia9/WhiteaBot/master/assets/whitea_rounded.png")
            
        await message.send(embed = embed)
        
def setup(bot):
    bot.add_cog(Help(bot))
    
