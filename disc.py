from dotenv import load_dotenv
import discord
import os
from discord.ext import commands
import asyncio

def post(MESSAGE,LINK,INTERVAL = 3000,CHANNEL = 345990055094910976):
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    def process(text):
        if len(text) < 1950:
            return text
        else:
            return text[:1950] + '...contd. on the forum link'
    
    client = discord.Client()

    @client.event
    async def on_ready():
        await client.change_presence(activity=discord.Game(name='with Heliohost RSS'))
        messageinterval = INTERVAL
        messagechannel = CHANNEL
        messagecontent = process(MESSAGE) + '\n' + LINK
        print('Message sent every: ' + str(messageinterval) + ' sec.')
        print('Destination channel id: ' + str(messagechannel))
        print('Message content: ' + str(messagecontent))

    async def send_interval_message():
        await client.wait_until_ready()
        channel = client.get_channel(CHANNEL)
        interval = INTERVAL
        message = process(MESSAGE) + '\n' + LINK
        while not client.is_closed():
            await channel.send(message)
            await asyncio.sleep(interval)

    async def list_servers():
        await client.wait_until_ready()
        while not client.is_closed():
            print("--- FEEDER IS ONLINE ---")
            for server in client.guilds:
                print('Active servers: ' + str(server.name))
            await asyncio.sleep(600)

    client.loop.create_task(send_interval_message())
    client.loop.create_task(list_servers())

    client.run(TOKEN)

if __name__ == '__main__':
    post('Hi there!')
