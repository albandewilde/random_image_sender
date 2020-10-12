# Critical Hit/Fumble cards for discord

Choose a random image to CRITICAL or FAIL situations and send it.

## Get our own bot

To get your own bot, follow these steps:
- download or clone this repository.
- copy the `env.json.tpl` file to `env.json`
- edit the `env.json` file
- replace `<your_images_folder>` by the relative folders path where your images are. Here I use the `./images/` and `./images_fail/` folders
- put all your images that can be send in the `images/` to critical and `images_fail/` to fail :).
- follow steps for the service you want (see below)

### Discord bot

- copy the `secrets.json.tpl` file to `secrets.json`
- edit the `secrets.json` file
- replace `<your_discord_token>` by your discord token
- save the file and quit
- start the bot with the command `python3 discord_client.py`

