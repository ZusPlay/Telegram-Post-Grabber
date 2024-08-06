# -*- coding: utf-8 -*-
import re
import json
import requests
from time import sleep
from os.path import abspath
from urllib.parse import quote_plus
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import openai

# Read config file
print("Reading config file...")
with open(abspath('config.json'), encoding='utf-8') as f:
    config = json.load(f)

# Check if config file is empty
if not (config['client']['api_id'] and config['client']['api_hash']
        and config['settings']['my_channels'] and config['settings']['chats']):
    print('Error! You missed something in the settings (config.json). Fill it out for proper operation.')
    exit()

# Read prompt from prompt.txt file
print("Reading prompt file...")
with open(abspath('prompt.txt'), encoding='utf-8') as f:
    edit_prompt = f.read().strip()

# Init OpenAI API
print("Initializing OpenAI API...")
openai.api_key = config['openai']['api_key']

def has_ban_phrases(text, ban_phrases):
    print("Checking for ban phrases...")
    # Split text into words, preserving spaces for multi-word phrase checks
    text_lines = text.split('\n')
    text_words = ' '.join(text_lines).split(' ')
    
    # Create a set of unique words for quick lookup
    sbuf = set(text_words)
    
    # Check for single words in the text
    single_word_bans = [x for x in ban_phrases if ' ' not in x and x in sbuf]
    
    # Check for multi-word phrases in the text
    multi_word_bans = [x for x in ban_phrases if ' ' in x and x in text]
    
    # Combine results from single words and multi-word phrases
    result = single_word_bans + multi_word_bans
    
    return bool(result)

def has_ban_symbols(text, ban_symbols):
    print("Checking for ban symbols...")
    if len(ban_symbols) == 0:
        return False
    pattern = '(?:{})'.format('|'.join(ban_symbols))
    return bool(re.search(pattern, text, flags=re.I))

def send_message(message):
    print(f"Sending message: {message}")
    if config['bot']['token'] and config['bot']['all_ID']:
        for user_id in config['bot']['all_ID']:
            url_message = quote_plus(message)
            response = requests.post(
                url="https://api.telegram.org/bot" + str(config['bot']['token']) + "/sendMessage?chat_id=" + str(
                    user_id) + "&text=" + str(url_message)
            ).json()
            print(f"Response from Telegram: {response}")

def edit_message(text):
    print("Editing message using OpenAI API...")
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": edit_prompt},
            {"role": "user", "content": text}
        ],
        max_tokens=500
    )
    edited_content = response.choices[0].message.content.strip()
    print(f"Edited message: {edited_content}")
    return edited_content

print(config['bot']['message'])
send_message(config['bot']['message'])

try:
    print("Starting Telegram client...")
    client = TelegramClient(StringSession(config['client']['string_session']), config['client']['api_id'], config['client']['api_hash'])
    client.start()
    print("Telegram client started.")

    @client.on(events.Album(chats=config['settings']['chats']))
    async def album_handler(event: events.Album.Event):
        print(f"Handling album event: {event}")
        sleep(config['settings']['timer'])
        for channel in config['settings']['my_channels']:
            await client.send_message(channel, file=event.messages, message=event.original_update.message.message)
            sleep(1)

    @client.on(events.NewMessage(chats=config['settings']['chats']))
    async def normal_handler(event: events.NewMessage.Event):
        print(f"Handling new message event: {event}")
        if event.message.media and event.grouped_id is not None:
            print("Message is part of an album, skipping...")
            return

        has_bw = has_ban_phrases(str(event.message.message), config['settings']['ban_phrases'])
        has_bs = has_ban_symbols(str(event.message.message), config['settings']['ban_symbols'])

        if not has_bw and not has_bs:
            print("Message passed ban checks.")
            sleep(config['settings']['timer'])
            for channel in config['settings']['my_channels']:
                print(f"Forwarding message to channel: {channel}")
                await client.send_message(channel, event.message)
                sleep(1)
                edited_text = edit_message(event.message.message)
                print(f"Sending edited message to channel: {channel}")
                await client.send_message(channel, edited_text)
                sleep(1)

    client.run_until_disconnected()
except Exception as error:
    send_message(f'An error occurred...\n\n{error}')
    print(f"Error: {error}\n")
