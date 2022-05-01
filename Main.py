import discord
import emoji
import time
TOKEN = 'OTcwMjAyMjM5NDc2MDcyNDY4.Ym4hPw.4CIJNUqxzAPjAIdpOSKopgLTc70'

client = discord.Client()

bad_words = []
zet = "https://www.instagram.com/justzetu/"
seby = "https://www.instagram.com/sebasti4n.exe/"

@client.event
async def on_ready():
    print('Ne-am logat ca {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.content == 'developers':
        await message.channel.send(f"{zet} \n {seby}")
        
client.run(TOKEN)
#am modificat codul
