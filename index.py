
import os

import discord
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_SECRET')

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


client.run(TOKEN)
