import discord
import os
import asyncio
import re

intents = discord.Intents.default()
client = discord.Client(intents=intents)
channelID = 819472181578432533
purge_command = "!purge"

@client.event
async def on_ready():
 '''Called wheTh client is ready. Prints the bot's current user.'''
 print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
       if message.author == client.user:
           return
       if (isinstance(message.channel,discord.DMChannel)):
           return
       if (message.author.bot or message.author.system):
           return
       if message.content == purge_command:
           if message.author.permissions_in(message.channel).manage_messages:
               await message.add_reaction("✅")
               async for x in (message.channel.history()):
                   if toDelete(x):
                       print(x.content)
                       if x.content != purge_command:
                           await x.delete()
               await message.delete()
               return
       if toDelete(message):
           print("deleting" + message.content)
           await message.delete()

def toDelete(message):
    image=False
    if isValidURL(message.content):
        image=True
    return message.channel.id == channelID and (len(message.attachments) == 0 and not image)

def isValidURL(url):
    regex = re.compile( #using django url validator
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)

client.run(os.getenv("TOKEN"))
