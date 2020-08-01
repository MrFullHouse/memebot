import asyncio
import discord
from discord.ext import commands
import json
import subprocess
import os
import datetime
import requests
import re
import random
from string import punctuation
import time

client = discord.Client()

with open('config.json') as config_data:
    config_json = json.load(config_data)
    token = config_json['discord_token']
    images_path = config_json['images_path']
    gif_path = config_json['gif_path']

phrases=['Ваш мем, сэр <:lambert:595522325152137220>','Твой мем, бомжара <:bonjour_epta:605476358407323658>','Хотел мема - подавись','Ставь кулсторибоба если не смешно <:coolstorybob:440201373410131978>',\
'Мемас?','Кто заказывал мемас?','Memes is three hundred bucks <:MRCO:589181415300792320>','Ставь лукаса если смешно','Я тебя ненавижу',\
'Если тебе смешно значит мем смешной woof','Кто следующий попросит мем тот еблан <:gravi:589177100125208617>','АЛЛО!',\
'Этот мем скинул полный даун конечно','Жиза?','Так то у меня свой бизнес, а мемы чисто для души отправляю',\
'<:coolstorybob:440201373410131978>','<:coolstorybob:440201373410131978>','Никак вы, блять, не научитесь <:geraltsleep:590156064654098433>','','','','','','','','','','','']
emojis=[]


@client.event
async def on_ready():
    for emoji in client.emojis:
        print('name:', emoji.name, 'id:', emoji.id)

@client.event
@asyncio.coroutine
def on_message(message):
    if message.author == client.user:
        return
################DOBRIIIIIIIIIIIIIK##########
    if message.content.startswith('!алло'):
        bob=client.get_emoji(440201373410131978)
        yield from message.add_reaction(bob)
        yield from message.channel.send('Алло, Кухня' + '<:pled:589174859326554122>')
    if message.content.startswith('!макросы'):
        yield from message.channel.send('хуякросы')
    if message.content.startswith('!хуякросы'):
        yield from message.channel.send('макросы')
    if message.content.startswith('!батя'):
        yield from message.channel.send('пошел нахуй, урод блять моральный. Ничего в жизни ен добился не создал ничего дял этого мира, ничего не привнес, батя он, вышел отсюда')
    if message.content.startswith('!Муурия'):
        yield from message.channel.send('<3')
#####mem
    if message.content.startswith('мам!мем'):
        bob=client.get_emoji(440201373410131978)
        for item in os.walk('%s' % (images_path) ):
            images=list(pic for pic in item[2])
            image=random.choice(images)
            phrase=random.choice(phrases)
            yield from message.channel.send(phrase, file=discord.File(images_path + image))
####dvamema
    if message.content.startswith('мам!двамема'):
        pog=client.get_emoji(460176998418087939)
        yield from message.add_reaction(pog)
        for item in os.walk('%s' % (images_path) ):
            images=list(pic for pic in item[2])
            image1=random.choice(images)
            image2=random.choice(images)
            phrase=random.choice(phrases)
            two_memes = [discord.File(images_path + image1),discord.File(images_path + image2),]
            yield from message.channel.send(phrase, files=two_memes)
####gif
    if message.content.startswith('мам!гиф'):
        for item in os.walk('%s' % (gif_path) ):
            images=list(pic for pic in item[2])
            image=random.choice(images)
            yield from message.channel.send('Автор - Таттз', file=discord.File(gif_path + image))
####count
    if message.content.startswith('мам!сколькомемов'):
        memcount=subprocess.Popen('sh /usr/local/discord/memebot/subshell.sh' , stdout=subprocess.PIPE, stderr=None, shell=True)
        stdout_value = memcount.communicate(input)
        yield from message.channel.send(stdout_value)

client.run(token)
