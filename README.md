# Grabber

## Documentation languages:

- [English](https://github.com/ZusPlay/Telegram-Post-Grabber/blob/main/README.md)
- [Українська](https://github.com/ZusPlay/Telegram-Post-Grabber/blob/main/README_ua.md)

## _Setup and Usage Guide_

Before running the program, we need to configure the config file.

Here is how the current config.json file looks:
```json
{
  "client": {
    "api_id": 0,
    "api_hash": ""
  },
  "bot": {
    "token": "",
    "all_ID": [],
    "message": ""
  },
  "settings": {
    "my_channels": [],
    "chats": [],
    "timer": 0,
    "ban_words": [],
    "ban_symbols": []
  }
}
```

### client
To obtain the data below, you need to go here:
[https://my.telegram.org/](https://my.telegram.org/),
log in here, then click "API development tools" and fill in the fields like [this](https://imgur.com/a/NCCkWrY),
and don't forget to check the Platform category as "Desktop."
- **api_id**: The first field, "App api_id," consists of numbers in the "App configuration" category.
  In the configuration, specify it as numbers. _Example:_ 123456789
- **api_hash**: The second field, "App api_hash," is a long text in the "App configuration" category.
  Specify it in the configuration as a string enclosed in quotes. _Example:_ "1a2b3c4_5#67s8fg9tty"
  [Examples of these fields](https://imgur.com/a/NjzxOYw)

### bot
- **token**: The token of your bot on Telegram, required for the bot's operation.
  The bot is intended to send users messages about the software's launch and any errors during its operation.
  You can obtain it [here](https://t.me/BotFather). Then create a new bot by sending the command ```/newbot```. Follow the instructions
  until you receive a username and token for your bot.
  You can access your bot by going to this URL: ```https://telegram.me/YOUR_BOT_USERNAME```
  and your token should look like this: ```704418931:AAEtcZ*************```
  Specify it in the configuration as a string enclosed in quotes. _Example:_ "703468982:AAEtcZ67s8fg9t3s4va4tty"
- **all_ID**: User IDs who will receive notifications from the bot
  (they need to interact with the bot at least once and press /start to receive notifications).
  You can obtain their IDs [here](https://t.me/myidbot) by forwarding a message from a person to the bot and copying the necessary ID.
  Specify them in the configuration as an array of numbers. _Example:_ [123456789, 234567890, 345678901]
- **message**: The notification that will be sent when the software is launched.
  Specify it in the configuration as a string enclosed in quotes. _Example:_ "Starting grabber..."

### settings
- **my_channels**: IDs of your channels where you want to send posts.
  You can obtain them [here](https://t.me/myidbot) by forwarding a message from the channel to the bot and copying the ID.
  Specify them in the configuration as an array of numbers. _Example:_ [123456789, -100234567890, -100345678901]
- **chats**: IDs of other channels from which you want to receive posts.
  You can obtain them [here](https://t.me/myidbot) by forwarding a message from the channel to the bot and copying the ID.
  Specify them in the configuration as an array of numbers. _Example:_ [-100123456789, 234567890, -100345678901]
- **timer**: The timer for how many seconds to send a post to a channel after another channel publishes it.
  Specify it in the configuration as numbers. Zero means no delay. _Example:_ 60
- **ban_words**: Words that will cause posts to be ignored.
  If any word from the list is found in a post, it will not be published.
  Specify them in the configuration as an array of strings enclosed in quotes. _Example:_ ["word1", "word2", "word3"]
- **ban_symbols**: Symbols that will cause posts to be ignored.
  If any combination of symbols from the list is found in a post, it will not be published.
  Specify them in the configuration as an array of strings enclosed in quotes. _Example:_ ["symbol1", "symbol2", "symbol3"]

Example of a filled config.json:
```json
{
  "client": {
    "api_id": 123456789,
    "api_hash": "1a2b3c4_5#67s8fg9tty"
  },
  "bot": {
    "token": "703468982:AAEtcZ67s8fg9t3s4va4tty",
    "all_ID": [123456789, 234567890, 345678901],
    "message": "Starting grabber..."
  },
  "settings": {
    "my_channels": [123456789, 234567890, 345678901],
    "chats": [123456789, 234567890, 345678901],
    "timer": 0,
    "ban_words": ["word1", "word2", "word3"],
    "ban_symbols": ["symbol1", "symbol2", "symbol3"]
  }
}
```

### First software launch

All actions below need to be done once or after you will be doing something with files.

When you run the software, you will be prompted to enter your phone number (or bot token):",
which you used above, and the confirmation code "Please enter the code you received: ".
If you have 2fa enabled, enter your password for it: " (it will not be displayed in the console, but the input works).

After that, it will write "Signed in successfully as ..." and the software will work.

### Software Launch

Launch the software, and it works!
