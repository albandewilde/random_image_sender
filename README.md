# Critical Hit/Fumble cards for discord

Choose a random image to CRITICAL or FAIL situations and send it.

## Get our own bot

To get your own bot, follow these steps:
- download or clone this repository.
- copy the `env.json.tpl` file to `env.json`
- edit the `env.json` file
- replace `<your_images_folder>` by the relative folders path where your images are. Here I use the `./images/` and `./images_fail/` folders
- put all your images that can be send in the `images_critical/` to critical and `images_fail/` to fail :)
- put the helper messages to use `help` commands in the correct folders `images_critical_helper/` to critical and `images_fail_helper/` to fail.
- follow steps for the service you want (see below)

### Discord bot

- copy the `secrets.json.tpl` file to `secrets.json`
- edit the `secrets.json` file
- replace `<your_discord_token>` by your discord token
- save the file and quit
- start the bot with the command `python3 discord_client.py`


### Example of cards/images to be used (portuguese)

- Você pode usar as seguintes cartas desenvolvida pelo pessoal do RPG NEXT no link abaixo, no meu caso fiz a separação das cartas de ajuda nas pastas corretas.

Falha
`https://drive.google.com/drive/folders/1I4OpT0hz_1SmmtoweAdf4N-7rHr8LRgc`


Critico
`https://drive.google.com/drive/folders/1Cd7f495KPHfOJQ0hp8usEWQmHTVpQYDg`
