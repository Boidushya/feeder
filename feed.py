import feedparser
from bs4 import BeautifulSoup as bs
from pprint import pprint
from hashlib import md5
import json
import os
import re
import discord
from dotenv import load_dotenv
import asyncio
load_dotenv()

url = 'https://www.helionet.org/index/rss/forums/1-heliohost-news/'

feed = feedparser.parse(url)

TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)
client = discord.Client()

def write(feed):
    counter = 0
    arr = []
    for i in range(len(feed['items'])):
        soup = bs(feed['items'][i]['summary'], 'html.parser')
        text = soup.get_text()
        enc = md5(text.encode())
        if not os.path.isfile('sub.dat'):
            f = open('sub.dat', 'w')
            f.close()
        val = check(enc.hexdigest(), 'sub.dat')
        with open('sub.dat', 'a+') as f:
            if not val:
                with open('sub.dat', 'a') as f:
                    ('Successfully encoded as ' + enc.hexdigest() + ' !')
                    f.write(enc.hexdigest() + '\n')
                    counter += 1
                    arr.append(text)
    return arr


def check(y, f):
    with open(f, 'r') as file:
        for line in file:
            if re.match(y, line):
                return True
    return False


def respond(a):
    if len(a) == 0:
        print('[!]No new RSS received...')
    else:
        print('[+]Received new Feed! Processing...')
        post(a)

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')
#     await client.change_presence(activity=discord.Game(name='with Heliohost RSS'))
#     channel = client.get_channel(345990055094910976)
#     await channel.send('hello')

def post(msg):
    # await client.change_presence(activity=discord.Game(name='with Heliohost RSS'))
    channel = client.get_channel(345990055094910976)
    # await channel.send('hello')



if __name__ == '__main__':
    # write(feed)
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    client.run(TOKEN)
