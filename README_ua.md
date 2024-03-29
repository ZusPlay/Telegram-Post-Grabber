# Граббер

## Мови документації:

- [English](https://github.com/ZusPlay/Telegram-Post-Grabber/blob/main/README.md)
- [Українська](https://github.com/ZusPlay/Telegram-Post-Grabber/blob/main/README_ua.md)


## _Інструкція з налаштування та використання_

Прежде чем запустить программу нам нужно настроить конфиг-файл.

Ото виглядає config.json на даний момент:
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
Для отримання нижченаведених даних, вам потрібно перейти сюди:
[https://my.telegram.org/](https://my.telegram.org/),
увійти в систему, потім натиснути "API development tools" і заповнити поля, як показано [тут](https://imgur.com/a/NCCkWrY),
не забудьте встановити позначку в категорії "Platform" на "Desktop".
- **api_id**: Перше поле, "App api_id", цифри, в категорії "App configuration".
  В конфігурації слід вказувати як цифри. _Приклад:_ 123456789
- **api_hash**: Друге поле, "App api_hash", великий текст, в категорії "App configuration".
  В конфігурації слід вказувати як рядок, в лапках. _Приклад:_ "1a2b3c4_5#67s8fg9tty"

[Приклади цих полів](https://imgur.com/a/NjzxOYw)
### bot
- **token**: Токен вашого бота в Telegram, який потрібен для роботи самого бота.
  Бот буде призначений для надсилання користувачам повідомлень про запуск програми і її помилки під час роботи.
  Токен можна отримати [тут](https://t.me/BotFather). Потім створіть нового бота, надіславши команду ```/newbot```. Дотримуйтеся інструкцій,
  поки не отримаєте ім'я користувача і токен для свого бота.
  Ви можете перейти до свого бота, перейшовши за посиланням: ```https://telegram.me/YOUR_BOT_USERNAME```
  і ваш токен має виглядати так: ```704418931:AAEtcZ*************```
  В конфігурації слід вказувати як рядок, в лапках. _Приклад:_ "703468982:AAEtcZ67s8fg9t3s4va4tty"
- **all_ID**: Ідентифікатори користувачів, які отримуватимуть повідомлення від бота
  (для отримання їхніх повідомлень їм слід хоча б раз увійти в бота і натиснути /start)
  Їх можна отримати [тут](https://t.me/myidbot), надіславши боту повідомлення від людини та скопіювавши необхідний ідентифікатор.
  В конфігурації слід вказувати як масив цифр. _Приклад:_ [123456789, 234567890, 345678901]
- **message**: Повідомлення, яке буде надходити при запуску програми.
  В конфігурації слід вказувати як рядок, в лапках. _Приклад:_ "Початок збирача..."
### settings
- **my_channels**: Ідентифікатори ваших каналів, в які ви хочете надсилати повідомлення.
  Їх можна отримати [тут](https://t.me/myidbot), надіславши боту повідомлення з каналу та скопіювавши необхідний ідентифікатор.
  В конфігурації слід вказувати як масив цифр. _Приклад:_ [123456789, -100234567890, -100345678901]
- **chats**: Ідентифікатори чужих каналів, з яких ви хочете отримувати повідомлення.
  Їх можна отримати [тут](https://t.me/myidbot), надіславши боту повідомлення з каналу та скопіювавши необхідний ідентифікатор.
  В конфігурації слід вказувати як масив цифр. _Приклад:_ [-100123456789, 234567890, -100345678901]
- **timer**: Таймер, через скільки секунд надсилати повідомлення в канал після публікації чужого каналу.
  В конфігурації слід вказувати як цифри. Нуль - без затримки. _Приклад:_ 60
- **ban_words**: Слова, за якими будуть ігноруватися повідомлення.
  Якщо в повідомленні буде знайдено слово зі списку, то повідомлення не буде опубліковане у вас.
  В конфігурації слід вказувати як масив рядків, в лапках. _Приклад:_ ["слово1", "слово2", "слово3"]
- **ban_symbols**: Символи, за якими будуть ігноруватися повідомлення.
  Якщо в повідомленні буде знайдено поєднання символів зі списку, то повідомлення не буде опубліковане у вас.
  В конфігурації слід вказувати як масив рядків, в лапках. _Приклад:_ ["символи1", "символи2", "символи3"]

Приклад заповненого config.json:
```json
{
  "client": {
    "api_id": 123456789,
    "api_hash": "1a2b3c4_5#67s8fg9tty"
  },
  "bot": {
    "token": "703468982:AAEtcZ67s8fg9t3s4va4tty",
    "all_ID": [123456789, 234567890, 345678901],
    "message": "Початок збирача..."
  },
  "settings": {
    "my_channels": [123456789, 234567890, 345678901],
    "chats": [123456789, 234567890, 345678901],
    "timer": 0,
    "ban_words": ["слово1", "слово2", "слово3"],
    "ban_symbols": ["символи1", "символи2", "символи3"]
  }
}
```

### Первый запуск софта

Все действия ниже нужно сделать 1 раз или после того, когда будете что-то делать с файлами. 

Когда вы запустите софт Вас попросит ввести номер "Please enter your phone (or bot token): ", 
который Вы использовали выше и код подтверждения "Please enter the code you received: ".
Если у Вас стоит 2fa, то введите от неё пароль "Please enter your password: " (он отображаться в консоли не будет, но ввод работает).

После этого Вам напишет "Signed in successfully as ..." и софт будет работать.

### Запуск софта

Запускаете софт и он работает!
