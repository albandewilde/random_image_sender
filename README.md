# RIS (Random Image Sender)
Choose a random image in a folder and send it.

You can get you own bot for differents reasons. For exemple, if you want to have your own image folder.
However, you can use the already existing services.

The bot can be use for many services.
- [x] Discord
- [ ] e-mail
- [ ] Twitter
- [ ] Messenger
- [x] Web site
- [ ] Irc
- [ ] ...

## Running services

### Discord

If you want that bot on your server, it is available on the [Discord Bot List](https://top.gg/ "DBL") at [this page](https://top.gg/bot/639976883148292136 "RIS").  
Otherwise you can invite him with [that link](https://discordapp.com/api/oauth2/authorize?client_id=639976883148292136&scope=bot&permissions=0 "invite RIS").

### Web site

The web site isn't hosted for now, if you want to host it for me be pleased to
contact me.

## Get our own bot

To get your own bot, follow these steps:
- download or clone this repository.
- copy the `env.json.tpl` file to `env.json`
- edit the `env.json` file
- replace `<your_images_folder>` by the relative folder path where your images are. Here I use the `./images/` folder
- put all your images that can be send in the `images/` folder.
- follow steps for the service you want (see below)

### Discord bot

- copy the `secrets.json.tpl` file to `secrets.json`
- edit the `secrets.json` file
- replace `<your_discord_token>` by your discord token
- save the file and quit
- start the bot with the command `python3 discord_client.py`

### Web site

#### Bottle

- edit the `env.json` file
- in the `bottle` section, replace `<host_the_server_run>` by the hostname your server run
- replace `<port_the_server_run>` by rhe port your server use to run
- save the file and quit
- start the server with the commant `python3 bottle_client.py`
