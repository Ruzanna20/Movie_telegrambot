# Telegram Movie Bot

A Telegram bot that allows users to search for movie information using the OMDB API. Users simply send a movie name, and the bot will return information about it.

## Features

- Accepts movie names
- Searches for movie information using the OMDB API
- Sends movie information back to the user on Telegram

## Tech Stack

- Python
- Telegram Bot API (python-telegram-bot)
- OMDB API
- Requests library

## Prerequisites

- Python 3.7+
- A Telegram bot token from BotFather (https://t.me/botfather)
- An OMDB API key (http://www.omdbapi.com/)

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/telegram-movie-bot.git
cd telegram-movie-bot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create a .env file in the root directory and add the following:

```
telegram_bot_token=your_telegram_bot_token_here
OMDB_API_key=your_omdb_api_key_here
```

## Running the Bot

To start the bot, run:

```bash
python bot.py
```

The bot will start polling for messages.

## Usage

- Send the `/start` command to the bot to begin
- Send the `/help` command for assistance
- Send a movie name to the bot on Telegram
- The bot will search for the movie and send back information about it

## Dependencies

- python-telegram-bot
- requests
- python-dotenv

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.

## Disclaimer

This bot is intended for personal use only. Use responsibly.
