from ctypes.wintypes import WORD
import discord
import variables.emoji as emoji
from variables.credits import *
import asyncio
import time

TOKEN = 'OTcwMjAyMjM5NDc2MDcyNDY4.Ym4hPw.skcw7GzRu1A15veIUQj0djrDHZw'

client = discord.Client()


salut = "Salute"

#mesaj logare bot - NU EDITA NIMIC!
@client.event
async def on_ready():
    print('Ne-am logat ca {0.user}'.format(client))



#Fraze de bun venit
@client.event
async def on_message(message):
    if str(message.content).lower() == 'hey':
        await message.channel.send("Bunăăă ♥")
    
    if str(message.content).lower() == 'salut':
        await message.channel.send("Salut! :)")

    if message.content == :
            await message.channel.send("Du-te'n pizda mamii mele")
    


#comenzi bot
    if message.content == '*developers':
        await message.channel.send(f"{zet, emoji.heart} \n {seby, emoji.heart}")


client.run(TOKEN)
#modificare