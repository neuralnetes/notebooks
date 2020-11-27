# discord server scraper

scrape a discord server
filter messages by user
tokenize the content of each message
look for tickers

# links

* [get-bot-token](img/bot-token.png)
* [discord-application](https://discord.com/developers/applications/781953254883459074/bot)
* [write-bots](https://www.writebots.com/discord-bot-token/)
* [terraform-provider-discord](https://registry.terraform.io/providers/aequasi/discord/latest/docs)

# environment variables

```
DISCORD_BOT_TOKEN
```

# environment setup

```
export DISCORD_BOT_TOKEN=NzgxOTUzMjU0ODgzNDU5MDc0.X8FItw.akkmdU7ZZeRtakHLDcM27W8U9bw
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```