# Telegram Bot for Soccer Match Notifications

This project is a Python script that uses the Telegram Bot API to send notifications about soccer matches that meet specific conditions. The script reads data from a JSON file containing soccer match information, checks if certain conditions are met, and sends notifications to a designated Telegram channel. The main purpose of this script is to notify users about matches where specific goal conditions are expected.

## Getting Started

### Prerequisites
- Python 3.x
- The `requests` library: Install it using `pip install requests`.
- The `pandas` library: Install it using `pip install pandas`.

### Setting Up
1. Clone this repository to your local machine or download the script directly.
2. Obtain a Telegram bot token by following the [official instructions](https://core.telegram.org/bots#botfather).
3. Create a Telegram channel or group where you want to receive the notifications. Add your bot as an administrator to that channel/group and note down the chat ID.
4. Place your JSON file (`partidas-22-08.json`) containing match data in the same directory as the script.

### Configuration
Replace the placeholder values in the script with your own values:

- `bot_token`: Replace with your Telegram bot token obtained from BotFather.
- `chat_id`: Replace with the chat ID of the channel/group where you want to receive notifications.

### Running the Script
1. Open a terminal/command prompt.
2. Navigate to the directory containing the script.
3. Run the script using `python script_name.py`, where `script_name.py` is the name of your script.

The script will continuously monitor the JSON file for new match data that meets the specified conditions and send notifications to the designated Telegram channel/group.

## How It Works

1. The script reads match data from the JSON file.
2. It checks if the match ID has already been notified to avoid duplicate notifications.
3. For each match, it checks if the specified goal conditions are met.
4. If the conditions are met and the match is about to start (within the specified time frame), a notification is composed.
5. The notification is sent to the Telegram channel/group using the Telegram Bot API.

## Customize
You can customize the script to add more conditions, change notification messages, or modify the time frame for notifications.

## Disclaimer
This project is for educational purposes and personal use only. The accuracy and timeliness of the match data are not guaranteed. Use at your own risk.

Feel free to fork, modify, and improve this project according to your needs. If you have any questions or suggestions, please feel free to open an issue or contribute to the project. Enjoy your soccer match notifications!
