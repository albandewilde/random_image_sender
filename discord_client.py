#!/usr/bin/env python3

import json
from datetime import datetime
from discord.ext import commands
import discord
from get_file import rdm

# read our environement variables
with open("env.json", "r") as env:
    ENV = json.load(env)

# set our environement variables
IMG_CRITICAL = ENV["images_critical"]
IMG_FAIL = ENV["images_fail"]

FAIL_COMMAND = ENV["fail_command"]
CRITICAL_COMMAND = ENV["critical_command"]

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
    else:    
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

bot = commands.Bot(
    command_prefix="*",
    description="Send a random image"
)


@bot.command(
    name=CRITICAL_COMMAND,
    description="Send an critical card! Good shit"
)
async def random_critical_image(context):
    log(context)
    try:
        msg_content = {
            "file": discord.File(
                IMG_CRITICAL + "/{}".format(rdm(IMG_CRITICAL))
            )
        }
    except FileNotFoundError:
        DISPLAY_ERROR("The folder `{}` was not found".format(IMG_CRITICAL))
        msg_content = {
            "content": "The folder with images is missing, sorry..."
        }
    except ValueError:
        DISPLAY_ERROR("The folder `{}` is empty".format(IMG_CRITICAL))
        msg_content = {"content": "The folder with images is totaly empty"}

    try:
        await context.send(**msg_content)
    except:
        DISPLAY_ERROR("Somethings went wrong")
        msg_content = {"content": "Somethings went wrongs, sorry.\n┬─┬ ︵ /(.□. \）"}
        await context.send(**msg_content)

@bot.command(
    name=FAIL_COMMAND,
    description="Send an fail card! Oh no..."
)
async def random_fail_image(context):
    log(context)
    try:
        msg_content = {
            "file": discord.File(
                IMG_FAIL + "/{}".format(rdm(IMG_FAIL))
            )
        }
    except FileNotFoundError:
        DISPLAY_ERROR("The folder `{}` was not found".format(IMG_FAIL))
        msg_content = {
            "content": "The folder with images is missing, sorry..."
        }
    except ValueError:
        DISPLAY_ERROR("The folder `{}` is empty".format(IMG_FAIL))
        msg_content = {"content": "The folder with images is totaly empty"}

    try:
        await context.send(**msg_content)
    except:
        DISPLAY_ERROR("Somethings went wrong")
        msg_content = {"content": "Somethings went wrons, sorry.\n┬─┬ ︵ /(.□. \）"}
        await context.send(**msg_content)


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.event
async def on_ready():
    print(
        COLORS["YELLOW"] +
        "I'm logged in as {name} !\n".format(name=bot.user.name) +
        COLORS["NEUTRAL"]
    )


bot.run(DISCORD_TOKEN)
