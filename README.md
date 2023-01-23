# LikeBot for Telegram

## System design

1. Porpose of the project:
This project is a simple bot for Telegram that allows you to like messages in a group chat. It is useful for group chats where you want to like messages but you don't want to use the "like" button because it is too big and it takes too much space.

1. Problem statement:

Telegram has a "like" button however it doesn't give you statistics about the number of likes a message has received. This is a problem because you can't know if a message is popular or not.

1. Solution:

The solution is to create a bot that allows you to like messages in a group chat. The bot will store the number of likes a message has received and it will show you the number of likes a message has received.

1. System requirements:

The system requirements are:

- The bot must be able to like messages in a group chat.

- The bot must be able to show the number of likes a message has received.

- The bot must be able to show the number of likes a message has received in a specific time interval.

- The bot must be able to show the number of likes a message has received in a specific time interval for a specific user.

1. System architecture:

The system architecture is:

- The bot is written in Python.
- The bot uses the [python-telegram-bot](https://python-telegram-bot.org/)
library.

- The bot uses a JSON file to store the number of likes a message has received.

- The bot uses a JSON file to store the number of likes a message has received in a specific time interval.

## Database design

1. Database schema:
|User_id|Message_id|Likes|Date|
|---|---|---|---|
|123456789|123456789|1|2020-01-01 00:00:00|

```json
{
    "likes": {
        "message_id_0": {
            "user_id": {
                "like": 1,
                "date": "2020-01-01 00:00:00"
            },
            "message_id_1": {
            "user_id": {
                "like": 1,
                "date": "2020-01-01 00:00:00"
            },
        }
    }
}
```

## Structure of the bot

The bot will have the following handlers:

- /start: This handler will be used to start the bot.
- /help: This handler will be used to show the help message.
- like: This handler will be used to like a message.

## List of tasks

### Task 1: Create a Class for the like database

1. Create a class for the like database.

Atributes:

- likes: This attribute will be used to store the number of likes a message has received.
- dislikes: This attribute will be used to store the number of dislikes a message has received.
- data: This attribute will be used to store the JSON file.

Methods:

- __init__: This method will be used to initialize the class and it will load the JSON file if it doesn't exist it will create it.
- add_like: This method will be used to add a like to a message in the database.
- add_dislike: This method will be used to add a dislike to a message in the database.
- remove_like: This method will be used to remove a like to a message in the database.
- remove_dislike: This method will be used to remove a dislike to a message in the database.
- get_likes: This method will be used to get the number of likes a message has received.
- get_dislikes: This method will be used to get the number of dislikes a message has received.
- add_image: This method will be used to add an image to a message in the database.

