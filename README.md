# RIS (Random Image Sender)
Choose a random image in a folder and send it.

You can get you own bot for differents reasons. For exemple, if you want to have your own image folder.
However, you can use the already existing services.

The bot can be use for many services.
- [x] Discord
- [x] e-mail
- [ ] Twitter
- [ ] Messenger
- [x] Web site
- [ ] Irc
- [ ] ...

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

### e-mail

- edit the `env.json` file
- in the `email` section, replace:
    - `<your_smtp_server_address>` by the address of your smtp server.
    - `<port_of_smtp_server>` by the port of your smtp server.
    - `<sender_email_address>` by the e-mail address of your sender client
    - `<password_of_email_client>` by the password of the client
- save the file and quit
- start the server with the commant `python3 email_client.py`


### Web site

#### Bottle

- edit the `env.json` file
- in the `bottle` section, replace `<host_the_server_run>` by the hostname your server run
- replace `<port_the_server_run>` by rhe port your server use to run
- save the file and quit
- start the server with the commant `python3 bottle_client.py`
