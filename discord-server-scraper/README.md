# discord server scraper

* scrape a discord server
* filter messages by user
* tokenize the content of each message
* look for tickers

# links

* [discord-application](https://discord.com/developers/applications/781953254883459074/bot)
* [write-bots](https://www.writebots.com/discord-bot-token/)
* [get-bot-token](file://img/bot-token.png)

# environment setup

setup `.env` file with the following environment variables...
```
DISCORD_BOT_TOKEN=
```

then
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```