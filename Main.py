import discord
import emoji
import time
TOKEN = 'OTcwMjAyMjM5NDc2MDcyNDY4.Ym4hPw.s34L6pxKw8AzSzF4Cnxni9mTYiY'

client = discord.Client()

#variabile
zet = "https://www.instagram.com/justzetu/"
seby = "https://www.instagram.com/sebasti4n.exe/"


#mesaj logare bot - NU EDITA NIMIC!
@client.event
async def on_ready():
    print('Ne-am logat ca {0.user}'.format(client))



#Fraze de bun venit
@client.event
async def on_message(message):
    if message.content == 'Salut':
        await message.channel.send("Bunăăă ♥")
    if message.content == 'SALUT':
        await message.channel.send("Bunăăă ♥")
    if message.content == 'Hei':
        await message.channel.send("Bunăăă ♥")
    if message.content == 'HEI':
        await message.channel.send("Bunăăă ♥")
    if message.content == 'Hey':
        await message.channel.send("Bunăăă ♥")
    if message.content == 'HEY':
        await message.channel.send("Bunăăă ♥")
    if message.content == 'salut':
        await message.channel.send("Bunăăă ♥")
    if message.content == 'hei':
        await message.channel.send("Bunăăă ♥")
    if message.content == 'hey':
        await message.channel.send("Bunăăă ♥")


#comenzi bot
    if message.content == '*developers':
        await message.channel.send(f"{zet, emoji.heart} \n {seby, emoji.heart}")


client.run(TOKEN)