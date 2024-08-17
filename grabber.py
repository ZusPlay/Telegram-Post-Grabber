# -*- coding: utf-8 -*-
import re
import json
import requests
from time import sleep
from os.path import abspath
from urllib.parse import quote_plus
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Read config file
with open(abspath('config.json'), encoding='utf-8') as f:
    config = json.load(f)

# Check if config file is empty
if not (config['client']['api_id'] or config['client']['api_hash']
        or config['settings']['my_channels'] or config['settings']['chats']):
    logging.error('Error! You missed something in the settings (config.json). Fill it out for proper operation.')
    exit()

# Read prompt from prompt.txt file
with open(abspath('prompt.txt'), encoding='utf-8') as f:
    edit_prompt = f.read().strip()

def has_ban_phrases(text, ban_phrases):
    text_lines = text.split('\n')
    text_words = ' '.join(text_lines).split(' ')
    sbuf = set(text_words)
    single_word_bans = [x for x in ban_phrases if ' ' not in x and x in sbuf]
    multi_word_bans = [x for x in ban_phrases if ' ' in x and x in text]
    result = single_word_bans + multi_word_bans
    return bool(result)

def has_ban_symbols(text, ban_symbols):
    if len(ban_symbols) == 0:
        return False
    pattern = '(?:{})'.format('|'.join(ban_symbols))
    return bool(re.search(pattern, text, flags=re.I))

def send_message(message):
    if config['bot']['token'] and config['bot']['all_ID']:
        for user_id in config['bot']['all_ID']:
            url_message = quote_plus(message)
            requests.post(
                url="https://api.telegram.org/bot" + str(config['bot']['token']) + "/sendMessage?chat_id=" + str(
                    user_id) + "&text=" + str(url_message)
            ).json()

logging.info(config['bot']['message'])
send_message(config['bot']['message'])

try:
    client = TelegramClient(StringSession(config['client']['string_session']), config['client']['api_id'], config['client']['api_hash'])
    client.start()

    @client.on(events.Album(chats=config['settings']['chats']))
    async def album_handler(event: events.Album.Event):
        sleep(config['settings']['timer'])
        for channel in config['settings']['my_channels']:
            await client.send_message(channel, file=event.messages, message=event.original_update.message.message)
            sleep(1)

    @client.on(events.NewMessage(chats=config['settings']['chats']))
    async def normal_handler(event: events.NewMessage.Event):
        if event.message.media and event.grouped_id is not None:
            return

        has_bw = has_ban_phrases(str(event.message.message), config['settings']['ban_phrases'])
        has_bs = has_ban_symbols(str(event.message.message), config['settings']['ban_symbols'])

        if not has_bw and not has_bs:
            sleep(config['settings']['timer'])
            for channel in config['settings']['my_channels']:
                await client.send_message(channel, event.message)
                sleep(1)

    client.run_until_disconnected()
except Exception as error:
    send_message(f'An error occurred...\n\n{error}')
    logging.error(f'An error occurred: {error}')
