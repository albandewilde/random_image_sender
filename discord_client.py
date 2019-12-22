#!/usr/bin/env python3.7

import json
from datetime import datetime

import discord.ext.commands

from get_file import rdm

# read our environement variables
with open("env.json", "r") as env:
    ENV = json.load(env)

# set our environement variables
IMG_FOLDER = ENV["images_folder"]

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

SIGN = (
    COLORS["RED"] + "/" +
    COLORS["YELLOW"] + "!" +
    COLORS["RED"] + "\\" +
    COLORS["NEUTRAL"] +
    " "
)


def DISPLAY_ERROR(error_msg):
    print(
        "\n" +
        SIGN +
        " " +
        COLORS["RED"] +
        error_msg +
        COLORS["NEUTRAL"] +
        "\n"
    )


def log(context):
    channel = context.message.channel
    author = context.message.author

    channel_type = str(channel.type)
    name = author.name
    discriminator = author.discriminator
    nickname = author.display_name

    pseudo = (
        COLORS["RED"] +
        name + "#" + discriminator +
        COLORS["NEUTRAL"] +
        " (aka. " +
        COLORS["BLUE"] +
        nickname +
        COLORS["NEUTRAL"] +
        ")"
    )

    date = "{:04}/{:02}/{:02} {:02}:{:02}:{:02}".format(
        datetime.now().year,
        datetime.now().month,
        datetime.now().day,
        datetime.now().hour,
        datetime.now().minute,
        datetime.now().second
    )
    date = COLORS["PURPLE"] + date + COLORS["NEUTRAL"]

    if channel_type in ["text"]:
        guild = channel.guild

        server = (
            COLORS["GREEN"] +
            guild.name +
            COLORS["NEUTRAL"]
        )
        channel = (
            COLORS["CYAN"] +
            channel.name +
            COLORS["NEUTRAL"]
        )
        where = "on the server {srv} in {chan}".format(
            srv=server,
            chan=channel
        )
    elif channel_type in ["private"]:
        where = "in " + COLORS["GREEN"] + "direct message" + COLORS["NEUTRAL"]
    else:    # channel_type in ["voice", "group", "news", "store"]
        print(
            COLORS["RED"] +
            "This isn't a channel we can send images" +
            COLORS["NEUTRAL"]
        )

    print("{psd} ask for an image {where} at {date}".format(
        psd=pseudo,
        where=where,
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
    description="Send an image"
)
async def random_image(context):
    log(context)
    if (
        str(context.message.channel.type) == "private" or
        context.message.channel.is_nsfw()
    ):
        try:
            msg_content = {
                "file": discord.File(
                    IMG_FOLDER + "/{}".format(rdm(IMG_FOLDER))
                )
            }
        except FileNotFoundError:
            DISPLAY_ERROR("The folder `{}` was not found".format(IMG_FOLDER))
            msg_content = {
                "content": "The folder with images is missing, sorry..."
            }
        except ValueError:
            DISPLAY_ERROR("The folder `{}` is empty".format(IMG_FOLDER))
            msg_content = {"content": "The folder with images is totaly empty"}
    else:
        msg_content = {"content": "Sorry, this channel isn't a NSFW channel"}

    try:
        await context.send(**msg_content)
    except:
        DISPLAY_ERROR("Somethings went wrong")
        msg_content = {"content": "Somethings went wrons, sorry.\n┬─┬ ︵ /(.□. \）"}
        await context.send(**msg_content)


@bot.event
async def on_ready():
    print(
        COLORS["YELLOW"] +
        "I'm logged in as {name} !\n".format(name=bot.user.name) +
        COLORS["NEUTRAL"]
    )


bot.run(DISCORD_TOKEN)
