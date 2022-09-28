# -*- coding: utf-8 -*-
import json
import requests
from time import sleep
from urllib.parse import quote_plus
from telethon import TelegramClient, events

with open('config.json', encoding='utf-8') as f:
    config = json.load(f)

if not (config['client']['api_id'] or config['client']['api_hash']
        or config['settings']['my_channels'] or config['settings']['chats']):
    print('Ошибка! Вы забыли что-то заполнить в настройках (config.json). Заполните их для нормальной работы.')
    input()
    exit()


def has_ban_words(text, ban_words):
    text_words = ' '.join(text.split('\n')).split(' ')
    sbuf = set(text_words)
    result = [x for x in ban_words if x in sbuf]
    return bool(result)


def send_message(message):
    if config['bot']['token'] and config['bot']['all_ID']:
        for user_id in config['bot']['all_ID']:
            url_message = quote_plus(message)
            requests.post(
                url="https://api.telegram.org/bot" + str(config['bot']['token']) + "/sendMessage?chat_id=" + str(
                    user_id) + "&text=" + str(url_message)
            ).json()


print(config['bot']['message'])
send_message(config['bot']['message'])

try:
    client = TelegramClient("Grabber", config['client']['api_id'], config['client']['api_hash'])
    client.start()  # client start


    @client.on(events.NewMessage(chats=config['settings']['chats']))
    async def normal_handler(event):
        # if isinstance(event.chat, types.Channel):
        if not has_ban_words(str(event.message.message), config['settings']['ban_words']):
            sleep(config['settings']['timer'])
            for channel in config['settings']['my_channels']:
                await client.send_message(channel, event.message)
                sleep(1)


    client.run_until_disconnected()
except Exception as error:
    send_message(str(f'Произошла какая-то ошибка...\n\n{error}'))
    print(error)
    print('\n')
