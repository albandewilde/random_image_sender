#!/usr/bin/env python3

import json
import discord
from discord.ext import commands

from get_file import rdm

# read our discord acces token
with open("secrets.json", "r") as secrets:
    DISCORD_TOKEN = json.load(secrets)["discord"]

bot = commands.Bot(command_prefix="¤")

@bot.command(name="img")
async def random_image(context):
    await context.send(file=discord.File("images/{}".format(rdm("images/"))))


@bot.event
async def on_ready():
    print("I'm logged in as {name} !".format(name=bot.user.name))


bot.run(DISCORD_TOKEN)
