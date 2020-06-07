#!/usr/bin/env python3

import smtplib
import imaplib
import json
from email.message import EmailMessage
from email import message_from_bytes
import imghdr
from datetime import datetime
from time import sleep

from get_file import rdm

# read env var
with open("env.json", "r") as env:
    ENV = json.load(env)

# set env var
IMG_FOLDER = ENV["images_folder"]

# email env
ENV = ENV["email"]
SERVER = ENV["server"]
SERVER_PORT = ENV["port"]
USER = ENV["address"]
PASSWORD = ENV["password"]

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


def DISPLAY_ERROR(error_msg):
    print(
        COLORS["RED"] +
        error_msg +
        COLORS["NEUTRAL"] +
        "\n"
    )


def time():
    date = "{:04}/{:02}/{:02} {:02}:{:02}:{:02}".format(
        datetime.now().year,
        datetime.now().month,
        datetime.now().day,
        datetime.now().hour,
        datetime.now().minute,
        datetime.now().second
    )

    return COLORS["BLUE"] + date + COLORS["NEUTRAL"]


def make_answer():
    """Create the message to send"""
    # Create the message and set a subject
    msg = EmailMessage()
    msg["Subject"] = "A random image."

    try:
        # Choose an image
        attachement = IMG_FOLDER + "/" + rdm(IMG_FOLDER)
        # Attach the image to the email
        with open(attachement, "rb") as img:
            img = img.read()
            msg.add_attachment(
                img,
                maintype="image",
                subtype=imghdr.what(None, img)
            )
    except Exception as err:
        msg.set_content("No image found")
        if isinstance(err, FileNotFoundError):
            DISPLAY_ERROR("`{}` directory is not found".format(IMG_FOLDER))
        elif isinstance(err, ValueError):
            DISPLAY_ERROR("`{}` directory is empty".format(IMG_FOLDER))
        else:
            DISPLAY_ERROR("An error occurred")

    return msg


def send_image(server, port, user, password, destinator):
    """Send the message to the destinator"""
    with smtplib.SMTP_SSL(server, port) as smtp:
        smtp.login(user, password)
        msg = make_answer()
        smtp.send_message(msg, user, destinator)


def reply(server, port, user, password):
    """Reply to all unread message"""
    with imaplib.IMAP4_SSL(server) as mail:
        mail.login(user, password)
        mail.select(readonly=False)
        _, data = mail.search(None, "(UNSEEN UNANSWERED)")

        for email_nb in data[0].split():
            _, data = mail.fetch(email_nb, "(RFC822)")
            dest = message_from_bytes(data[0][1])["From"]
            print("{} ask for an image at {}".format(
                COLORS["YELLOW"] + dest + COLORS["NEUTRAL"],
                time()
            ))
            send_image(server, port, user, password, dest)


if __name__ in "__main__":
    # That is the worst code i've ever wrote
    while True:
        try:
            reply(SERVER, SERVER_PORT, USER, PASSWORD)
        except Exception as err:
            print(err)
            print("An error occured, now waiting 60 secondes")
            sleep(60)
