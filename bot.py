# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 09:05:16 2020

@author: bourgeade adrien
test
"""

import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Salutations {member.name}! Je te souhaite la bienvenue mon cher ami sur {guild.name}!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    list_of_help = ('Moi, la Sainte Banane, je vais te dire comment m\'invoquer: '
                   '\n - divination! : permet de répondre à une de tes questions')

    list_of_divin = [
        'As-tu vraiment besoin de poser la question ? Oui...',
        'Assurément c\'est un superbe OUI',
        'Oui',
        'Oui, mais il n\'empêche que j\'aime me beurrer la biscotte!',
        ('Vous savez, moi je ne crois pas qu\'il y ait de bonne ou de mauvaise situation. Moi, si je devais résumer ma vie aujourd\'hui avec vous,'
        'je dirais que c\'est d\'abord des rencontres. Des gens qui m\'ont tendu la main, peut-être à un moment où je ne pouvais pas, où j\'étais'
        'seul chez moi. Et c\'est assez curieux de se dire que les hasards, les rencontres forgent une destinée... Parce que quand on a le goût'
        'de la chose, quand on a le goût de la chose bien faite, le beau geste, parfois on ne trouve pas l\'interlocuteur en face je dirais,'
        'le miroir qui vous aide à avancer. Alors ça n\'est pas mon cas, comme je disais là, puisque moi au contraire, j\'ai pu : et je dis'
        'merci à la vie, je lui dis merci, je chante la vie, je danse la vie... je ne suis qu\'amour ! Et finalement, quand beaucoup de gens'
        'aujourd\'hui me disent « Mais comment fais-tu pour avoir cette humanité ? », et bien je leur réponds très simplement, je leur dis que'
        'c\'est ce goût de l\'amour ce goût donc qui m\'a poussé aujourd\'hui à entreprendre une construction mécanique, mais demain qui sait ?'
        'Peut-être simplement à me mettre au service de la communauté, à faire le don, le don de soi...'),
        'Franchement... Là... Je suis au regret de t\'annoncer que je ne sais pas',
        'Bon, c\'est simple. Vous suivez les baffes. Et la réponse devrait être au bout. J\'vous accompagne pas hein, j\'vais rester là et réfléchir un peu.',
        'Aucune idée ^^\"',
        'Pioooou, la résolution exacte des équations de Navier-Stokes aurait été plus facile pour celle là! ',
        'Non... (On dit qu\'il n y a pas de question con... mais là! c\'est différent)',
        'Non!',
        'Mais ça ne va pas la tête?! Bien sûr que c\'est NON!',
        'Ahahahah, tu connais toi même la réponse! ;p',
        'Non, mais à l\'occasion, je vous mettrai bien un petit coup de polish!',
        'Quelle question répugante! je ne m\'abaisserais pas à répondre!',
        'Ma maman disais toujours que: \"la vie, c\'est comme une boite de chocolats, on ne sait jamais sur quoi on va tomber\"'
    ]

    if  'divination!' in message.content:
        response = random.choice(list_of_divin)
        await message.channel.send(response)

    if message.content == 'Aide moi sainte banane':
        await message.channel.send(list_of_help)

    if message.content.startswith('Salutations'):
        await message.channel.send('(Désolé de cette interruption mais un \"Salut!\" fût été plus court)')


client.run(TOKEN)
