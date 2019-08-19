import asyncio
import discord
import json
import subprocess
import os
import datetime
import requests
import re
from string import punctuation
from bs4 import BeautifulSoup
import time

client = discord.Client()
with open('config.json') as config_data:
    config_json = json.load(config_data)
    token = config_json['discord_token']

@client.event
@asyncio.coroutine
def on_ready():
#On ready, joins all servers in JSON
    for x in config_json['servers']:
        client.accept_invite(x)
        print(x)
        print('Logged in as')
        print(client.user.name)
        print('---------')
    
@client.event
@asyncio.coroutine 
def on_message(message):
    author = message.author
    if message.content.startswith('!алло'):
        yield from client.send_message(message.channel, 'Алло, Кухня')
    if message.content.startswith('!макросы'):
        yield from client.send_message(message.channel, 'хуякросы')
    if message.content.startswith('!хуякросы'):
        yield from client.send_message(message.channel, 'макросы')

client.run(token)
