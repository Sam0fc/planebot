import discord
import os
import asyncio

intents = discord.Intents.default()
client = discord.Client(intents=intents)
fileExt = [".png",".jpg",".jpeg",".gif",".bmp",".tiff"]
channelID = 819472181578432533

@client.event
async def on_ready():
 '''Called wheTh client is ready. Prints the bot's current user.'''
 print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
       if message.author == client.user:
           return
       if message.content == "!purge":
           async for x in (message.channel.history()):
               if toDelete(x):
                   print("deleting"+x.content)
                   if x.content != "!purge":
                       await x.delete()
           return
       if toDelete(message):
           await message.delete()

def toDelete(message):
    image=False
    for i in fileExt:
        if i in message.content.lower():
            print("found")
            image=True
    return message.channel.id == channelID and (len(message.attachments) == 0 and not image)


client.run(os.getenv("TOKEN"))
