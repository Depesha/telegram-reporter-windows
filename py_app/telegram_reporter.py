import asyncio
import random
import json
import pathlib

from os import system
from pathlib import Path
from telethon import TelegramClient
from telethon import functions, types
from report_text import generate_text

system('cls')

threads = 35

path = Path()
absolutePath = path.parent.absolute()
settings = json.loads(open(f"{absolutePath}\settings.json", 'r').read())

client = TelegramClient('session_new', settings['appId'], settings['apiHash'])
client.start()

reportChannelsPath = f'{absolutePath}\\#repoted_channels.txt'

print('Bot started')

async def main():
    number_of_channels_rep = 150

    telegram_list = open(reportChannelsPath, 'r').readlines()
    random.shuffle(telegram_list)

    for (i,telegram_channel) in enumerate(telegram_list[:number_of_channels_rep]):
        if "https://" in telegram_channel:
            telegram_channel = telegram_channel.split('/')[-1]
        elif '@' in telegram_channel:
            telegram_channel = telegram_channel[1:]

        telegram_channel = telegram_channel.strip()

        try:
            print(f"Reporting {telegram_channel}...")
            result = await client(functions.account.ReportPeerRequest(
                peer=telegram_channel,
                reason=types.InputReportReasonSpam(),
                message=generate_text())
            )

            print(f"Telegram channel {telegram_channel} is reported successfully. Channels left {len(telegram_list) - i}")
        except ValueError:
            print("Channel not found")

        await asyncio.sleep(random.randint(0, 2))

with client:

    client.loop.run_until_complete(main())



