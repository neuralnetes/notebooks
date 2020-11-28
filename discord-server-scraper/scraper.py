import os
import asyncio
import discord
from dotenv import load_dotenv


class DiscordClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        channel = discord.utils.get(self.get_all_channels(), guild__name='stonky-people', name='general')
        print(channel)

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


async def main():
    load_dotenv()
    token = os.environ['DISCORD_BOT_TOKEN']
    client = DiscordClient()
    return asyncio.gather(
        client.start(
            token,
            bot=True
        )
    )
