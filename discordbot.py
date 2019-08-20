import asyncio
import discord
import json
import subprocess
import os
import datetime
import requests
import re
import random
from string import punctuation
from bs4 import BeautifulSoup
import time

client = discord.Client()
with open('config.json') as config_data:
    config_json = json.load(config_data)
    token = config_json['discord_token']
    images_path = config_json['images_path']

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
        print(images_path)

@client.event
@asyncio.coroutine
def send_image(message):
    for item in os.walk('%s' % (images_path) ):
        images=list(pic for pic in item[2])
        image=random.choice(images)
        yield from client.send_file(message.channel,images_path + image)

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
    if message.content.startswith('мам!мем!'):
#        await send_image()
        yield from send_image(message)
    if message.content.startswith('мам!сколькомемов'):
        memcount=subprocess.Popen('ls %s | wc -l' % (images_path), shell=True)
        yield from client.send_message(message.channel, "В базе %s.stdout мемов" % (memcount))

client.run(token)
