**About**

This bot is focused on spamming messages.

Enviromental variables that are needed to be filled into `.env` file:
* DISCORD_TOKEN - Token for Discord bot from Discord Developer Portal
* DISCORD_GUILD - Name of Discord server
* LOG_CHANNEL - Channel for logging
* WELCOME_CHANNEL - Channel for welcoming users
* STORNO_CHANNEL - Channel for spamming

**Extensions**

Extensions in terms of `discord.ext.commands.Cog` can be added. It is needed to add a `Cog` in a python file to the `extensions` folder and add name of the python file to `extensions` array in `config\config.py`.

**Prerequisities**

* python => 3.6
* python3-pip (sudo apt-get install python3-pip)
* virtualenv (sudo pip3 install virtualenv)

**How to run**

1. python3 -m venv env
2. source env/bin/activate
3. pip3 install -r requirements.txt
4. python3 bot.py