#!/usr/bin/env python3.7

import json
from datetime import datetime

import discord.ext.commands

from get_file import rdm

COLORS = {
    "BLACK": "\033[30m",
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "PURPLE": "\033[35m",
    "CYAN": "\033[36m",
    "GREY": "\033[37m",
    "WHITE": "\033[38m",
    "NEUTRAL": "\033[00m"
}

def log(context):
    pseudo = COLORS["RED"] + context.message.author.name + COLORS["NEUTRAL"]
    server = COLORS["GREEN"] + context.message.channel.guild.name + COLORS["NEUTRAL"]
    channel = COLORS["CYAN"] + context.message.channel.name + COLORS["NEUTRAL"]
    date = "{}/{}/{} {}:{}:{}".format(
        datetime.now().year,
        datetime.now().month,
        datetime.now().day,
        datetime.now().hour,
        datetime.now().minute,
        datetime.now().second
    )
    date = COLORS["PURPLE"] + date + COLORS["NEUTRAL"]

    print("{psd} ask for an image on the server {srv} in {chan} at {date}".format(
        psd=pseudo,
        srv=server,
        chan=channel,
        date=date
    ))


# read our discord acces token
with open("secrets.json", "r") as secrets:
    DISCORD_TOKEN = json.load(secrets)["discord"]

bot = discord.ext.commands.Bot(
    command_prefix="¤",
    description="Send a random image"
)

@bot.command(
    name="img",
    pass_context=True,
    description="Send an image"
)
async def random_image(context):
    log(context)
    await context.send(file=discord.File("images/{}".format(rdm("images/"))))


@bot.event
async def on_ready():
    print(
        COLORS["YELLOW"] +
        "I'm logged in as {name} !\n".format(name=bot.user.name) +
        COLORS["NEUTRAL"]
    )


bot.run(DISCORD_TOKEN)
