import importlib
import os

import discord
from discord.ext import commands

from games.werewolf.gamehandler import GameHandler

intents = discord.Intents.default()
intents.members = True

if os.getenv('CLIENT') == 'production':
    prefix = '-'
else:
    prefix = '.'

client = commands.Bot(command_prefix=prefix, intents=intents)
handler = GameHandler(client=client)

async def register_commands():
    for folder in os.listdir('commands'):
        module = importlib.import_module(f'commands.{folder}.command')
        module.register(client=client)
    
async def register_games():
    for folder in os.listdir('games'):
        handler = importlib.import_module(f'games.{folder}.gamehandler')
        await handler.register(client=client)

@client.event
async def on_ready():
    await register_commands()
    await register_games()


TOKEN = os.getenv('CLIENT_TOKEN')
client.run(TOKEN)
