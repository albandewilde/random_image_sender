#!/usr/bin/env python3.7

import json

import bottle

from get_file import rdm

serv = bottle.Bottle()

# read our environement variables
with open("env.json", "r") as env:
    ENV = json.load(env)

# set our environement variables
IMG_FOLDER = ENV["images_folder"]
HOST = ENV["bottle"]["host"]
PORT = ENV["bottle"]["port"]


@serv.get("/")
def img():
    try:
        pics = rdm(IMG_FOLDER)
        content = "<img src='image/{image}' style='max-width: 100vw; max-height: 100vh;'>".format(image=pics)
    except FileNotFoundError:
        content = "Sorry, the folder with the images is not present"
    except ValueError:
        content = "There is currently no images"

    return """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>RIS</title>
    </head>
    <body>
        <center>
            {content}
        </center>
    </body>
</html>
    """.format(content=content)


@serv.get("/image/<image>")
def static(image):
    return bottle.static_file(image, root=IMG_FOLDER)


serv.run(host=HOST, port=PORT)
