#!/usr/bin/env python3

import json
from datetime import datetime
from discord.ext import commands
import discord
from get_file import rdm

# read our environment variables
with open("env.json", "r") as env:
    ENV = json.load(env)

# set our environment variables
FOLDER_CRITICAL = ENV["folder_critical"]
FOLDER_CRITICAL_HELPER = ENV["folder_critical_helper"]
FOLDER_FAIL = ENV["folder_fail"]
FOLDER_FAIL_HELPER = ENV["folder_fail_helper"]

COMMAND_FAIL = ENV["command_fail"]
COMMAND_CRITICAL = ENV["command_critical"]
COMMAND_FAIL_HELPER = ENV["command_fail_helper"]
COMMAND_CRITICAL_HELPER = ENV["command_critical_helper"]

COMMAND_CHAR = ENV['command_char']  # Command used to activate bot on discord


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
    command_prefix=COMMAND_CHAR,
    description="Send a random image"
)


# CRITICAL COMMANDS ================
@bot.command(
    name=COMMAND_CRITICAL,
    description="Send an critical card! Good shit"
)
async def random_critical_image(context):
    await send_img(FOLDER_CRITICAL, context)


@bot.command(
    name=COMMAND_CRITICAL_HELPER,
    description="Send an help for critical command!"
)
async def critical_help_image(context):
    await send_img(FOLDER_CRITICAL_HELPER, context)


# FAIL COMMANDS =====================
@bot.command(
    name=COMMAND_FAIL,
    description="Send an fail card! Oh no..."
)
async def random_fail_image(context):
    await send_img(FOLDER_FAIL, context)    


@bot.command(
    name=COMMAND_FAIL_HELPER,
    description="Send an help for critical command!"
)
async def critical_help_image(context):
    await send_img(FOLDER_FAIL_HELPER, context)



async def send_img(folder, context):
    log(context)
    try:
        msg_content = {
            "file": discord.File(
                folder + "/{}".format(rdm(folder))
            )
        }
    except FileNotFoundError:
        DISPLAY_ERROR("The folder `{}` was not found".format(folder))
        msg_content = {
            "content": "The folder with images is missing, sorry..."
        }
    except ValueError:
        DISPLAY_ERROR("The folder `{}` is empty".format(folder))
        msg_content = {"content": "The folder with images is totaly empty"}

    try:
        await context.send(**msg_content)
    except:
        DISPLAY_ERROR("Somethings went wrong")
        msg_content = {"content": "Somethings went wrongs, sorry.\n┬─┬ ︵ /(.□. \）"}
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
