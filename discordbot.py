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
    sep_path = config_json['sep_path']

phrases=['Ваш мем, сэр <:lambert:595522325152137220>','Твой мем, бомжара <:bonjour_epta:605476358407323658>','Хотел мема - подавись','Ставь кулсторибоба если не смешно <:coolstorybob:440201373410131978>',\
'Мемас?','Кто заказывал мемас?','Memes is three hundred bucks <:MRCO:589181415300792320>','Ставь лукаса если смешно','Я тебя ненавижу',\
'Если тебе смешно значит мем смешной woof','Кто следующий попросит мем тот еблан <:gravi:589177100125208617>','АЛЛО!',\
'Этот мем скинул полный даун конечно','Жиза?','Так то у меня свой бизнес, а мемы чисто для души отправляю',\
'<:coolstorybob:440201373410131978>','<:coolstorybob:440201373410131978>','Никак вы, блять, не научитесь <:geraltsleep:590156064654098433>','','','','','','','','','','','']
phrasesthree=['Ваш мем оказался предателем <:danceAmongUs:758389940664270938>','Через 5 минут сумка','Я ведь лучше чем дино? <:sadcat:589174859087478784> ','Я знаю что вы тут андерграунд, и я вас уважаю.',\
'Ради бога, напишите хоть кто-нибудь что мем говно','НУ ЗАЧЕМ ТЕБЕ ТРИ МЕМА!!!!!!!!','Ведется набор в ботнет на серьезное обеспечение, в планах захватить мир, гс в пм','Ты вообще в курсе что люди должны РАБОТАТЬ?','!рулетка',\
'Да ты добился хоть чего-нибудь чтоб заслужить эти мемы:','Если ниже будет рефейс, то ты гей','АЛЛО!',\
'Три мема. В три раза больше ненависти ко мне...','Три мема. В три раза больше боянов...',\
'Никак вы, блять, не научитесь <:geraltsleep:590156064654098433>','','','','','','','','','','','']
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
    if message.content.lower().startswith('!алло'):
        bob=client.get_emoji(440201373410131978)
        yield from message.add_reaction(bob)
        yield from message.channel.send('Алло, Кухня' + '<:pled:589174859326554122>')
    if message.content.lower().startswith('!макросы'):
        yield from message.lower().channel.send('хуякросы')
    if message.content.lower().startswith('!хуякросы'):
        yield from message.channel.send('макросы')
    if message.content.lower().startswith('!батя'):
        yield from message.channel.send('пошел нахуй, урод блять моральный. Ничего в жизни ен добился не создал ничего дял этого мира, ничего не привнес, батя он, вышел отсюда')
    if message.content.lower().startswith('!муурия'):
        yield from message.channel.send('<3')
#####mem
    if message.content.lower().startswith('мам!мем') or message.content.lower().startswith('мем!'):
        for item in os.walk('%s' % (images_path) ):
            images=list(pic for pic in item[2])
            image=random.choice(images)
            phrase=random.choice(phrases)
            yield from message.channel.send(phrase, file=discord.File(images_path + image))
####dvamema
    if message.content.lower().startswith('мам!двамема') or message.content.lower().startswith('2мема!'):
        pog=client.get_emoji(460176998418087939)
        yield from message.add_reaction(pog)
        for item in os.walk('%s' % (images_path) ):
            images=list(pic for pic in item[2])
            image1=random.choice(images)
            image2=random.choice(images)
            phrase=random.choice(phrases)
            two_memes = [discord.File(images_path + image1),discord.File(images_path + image2),]
            yield from message.channel.send(phrase, files=two_memes)
    if message.content.lower().startswith('мам!змема') or message.content.lower().startswith('3мема!'):
        glad=client.get_emoji(456530308972412928)
        yield from message.add_reaction(glad)
        for item in os.walk('%s' % (images_path) ):
            images=list(pic for pic in item[2])
            image1=random.choice(images)
            image2=random.choice(images)
            image3=random.choice(images)
            phrasethree=random.choice(phrasesthree)
            three_memes = [discord.File(images_path + image1),discord.File(images_path + image2),discord.File(images_path + image3),]
            yield from message.channel.send(phrasethree, files=three_memes)
####3_september
#    if message.content.startswith('мам!3сентября'):
#        shuf=client.get_emoji(750803276475269150)
#        yield from message.add_reaction(shuf)
#        for item in os.walk('%s' % (sep_path) ):
#            images=list(pic for pic in item[2])
#            image=random.choice(images)
#            yield from message.channel.send('<:shufutinskiy:750803276475269150>', file=discord.File(sep_path + image))
####gif
    if message.content.lower().startswith('мам!гиф') or message.content.lower().startswith('гиф!'):
        for item in os.walk('%s' % (gif_path) ):
            images=list(pic for pic in item[2])
            image=random.choice(images)
            yield from message.channel.send('Автор - Таттз', file=discord.File(gif_path + image))
####da-pizda
#
    if message.content.lower() == 'да':
        p=client.get_emoji(837420439553966100)
        i=client.get_emoji(837420438690463805)
        z=client.get_emoji(837420439533256714)
        d=client.get_emoji(837420439215013909)
        a=client.get_emoji(837420439843897410)

        yield from message.add_reaction(p)
        yield from message.add_reaction(i)
        yield from message.add_reaction(z)
        yield from message.add_reaction(d)
        yield from message.add_reaction(a)

    if message.content.lower() == 'пизда':
        d=client.get_emoji(837420439215013909)
        a=client.get_emoji(837420439843897410)
        yield from message.add_reaction(d)
        yield from message.add_reaction(a)

####count
    if message.content.lower().startswith('мам!сколькомемов') or message.content.lower().startswith('сколькомемов?'):
        memCount=subprocess.Popen('sh /usr/local/discord/memebot/subshell.sh' , stdout=subprocess.PIPE, stderr=None, shell=True)
        stdout_value = memCount.communicate(input)
        yield from message.channel.send(stdout_value)

client.run(token)
