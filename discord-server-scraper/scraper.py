import os
import discord
from dotenv import load_dotenv
from collections import defaultdict

"""
Stock Terms
SS - Short Sale
Blue Chip - Large Companies, Usually $50BN+ in Size
OTC - Over the counter, shit stocks, penny stocks that are not registered
Support -  Where there is more buying
Resistance - Where there is more selling
SL - Stop Loss
VWAP - Volume weighted average price
MACD - Moving Average Convergence Divergence
RSI - Relative Strength Index
EMA - Exponential Moving Average
MA - Moving average
PT - Price Target
"""
stock_terms = {
    'SS': 'Short Sale',
    'Blue Chip': 'Large Companies, Usually $50BN+ in Size',
    'OTC': 'Over the counter, shit stocks, penny stocks that are not registered',
    'Support': 'Where there is more buying',
    'Resistance': 'Where there is more selling',
    'SL': 'Stop Loss',
    'VWAP': 'Volume weighted average price',
    'MACD': 'Moving Average Convergence Divergence',
    'RSI': 'Relative Strength Index',
    'EMA': 'Exponential Moving Average',
    'MA': 'Moving average',
    'PT': 'Price Target',
}

"""
Options Terms
BTO - Buy to Open
STC - Sell to Close
STO - Sell to Open
BTC - Buy to Close
Expiration Date - The date in which my contract will become worthless if not exercised by (Why Options are Higher Risk and Reward)
Strike Price - The price in which I can buy or sell the stock if I choose to exercise my contract
"""
options_terms = {
    'BTO': 'Buy to Open',
    'STC': 'Sell to Close',
    'STO': 'Sell to Open',
    'BTC': 'Buy to Close',
    'Expiration Date': 'The date in which my contract will become worthless if not exercised by (Why Options are Higher Risk and Reward)',
    'Strike Price': 'The price in which I can buy or sell the stock if I choose to exercise my contract'
}


class DiscordClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


async def fetch_channel_messages(client: DiscordClient, channel_id: int):
    channel = await client.fetch_channel(channel_id)
    messages = await channel.history().flatten()
    return messages


def group_messages_by_author(messages):
    grouped = defaultdict(list)
    for message in messages:
        grouped[message.author.name].append(message)
    return grouped


async def main():
    load_dotenv()
    discord_token = os.environ['DISCORD_TOKEN']
    discord_bot = os.environ['DISCORD_BOT'] == 'true'
    # discord_guild_id = 542224582317441034
    discord_channel_id = 592829914022150146
    client = DiscordClient()
    await client.login(
        discord_token,
        bot=discord_bot
    )
    messages = await fetch_channel_messages(client, discord_channel_id)
    grouped_by_author = group_messages_by_author(messages)
    print(grouped_by_author)
