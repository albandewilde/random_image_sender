# RIS (Random Image Sender)
Choose a random image in a folder and send it.

You can get you own bot for differents reasons. For exemple, if you want to have your own image folder.
However, you can use the already existing services.

The bot can be use for many services.
- [x] Discord
- [ ] e-mail
- [ ] Twitter
- [ ] Messenger
- [ ] Web site
- [ ] ...

## Get our own bot

To get your own bot, follow these steps:
- download or clone this repository.
- put all your images that can be send in the `images/` folder.
- follow steps for the service you want (see below)

### Discrod bot

- copy the `secrets.json.tpl` file to `secrets.json`
- edit the `secrets.json` file
- replace the `<your_discord_token>` by your discord token
- save the file and quit
- start the bot with the command `python3 discord_client.py`
