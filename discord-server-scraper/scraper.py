import os
import asyncio
import discord
from dotenv import load_dotenv


class DiscordClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


async def get_channel_history(client: DiscordClient, channel_id: int):
    channel = await client.get_channel(channel_id)
    messages = await channel.history().flatten()
    print(messages)
    return messages


async def main():
    load_dotenv()
    discord_token = os.environ['DISCORD_TOKEN']
    discord_bot = os.environ['DISCORD_BOT'] == 'true'
    discord_channel_id = 592829914022150146
    client = DiscordClient()
    _ = await client.start(
        discord_token,
        bot=discord_bot
    )
    return get_channel_history(client, discord_channel_id)
