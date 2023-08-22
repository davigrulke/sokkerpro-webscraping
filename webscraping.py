import json
import pandas as pd
import requests
from datetime import datetime, timedelta
import time

# Define your Telegram bot token and chat ID
bot_token = "YOUR_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"  # Replace with your channel's ID

# List to track games that have already been notified
notified_games = []

# Continuously loop with a verification interval (e.g., every 2 minutes)
while True:
    # Read the JSON file
    with open('/content/partidas-22-08.json') as f:
        data = json.load(f)

    # Original time zone (+3)
    original_timezone = timedelta(hours=3)

    for entry in data['data']:
        game_id = entry['id']  # Get the game ID
        if game_id in notified_games:
            continue  # Skip the game if already notified

        goals05ht = entry['goals05ht']  # Get the value of goals05ht
        goals15ht = entry['goals15ht']  # Get the value of goals15ht
        if goals05ht >= 80 and goals15ht >= 60:  # Check the conditions
            home_team_name = entry['localTeam']['name']
            visitor_team_name = entry['visitorTeam']['name']
            match_datetime = datetime.strptime(entry['starting_time'], "%Y-%m-%d %H:%M:%S")
            adjusted_match_datetime = match_datetime - original_timezone

            # Calculate the time difference until the start of the game (10 minutes)
            time_until_match = (match_datetime - datetime.now()).total_seconds()
            time_to_send = 10 * 60  # 10 minutes in seconds

            if 0 <= time_until_match <= time_to_send:
                # Get the league name of the game
                league_name = entry['league_name']

                # Format the message to send to Telegram
                message = ("🔔 NEW OVER 0.5 HT OPPORTUNITY ABOUT TO START\n\n"
                          f"📰 Data Source: SokkerPro\n"
                          f"🏆 League: {league_name}\n"
                          f"⏰ Time: {adjusted_match_datetime.time()}\n"
                          f"🏠 Home Team: {home_team_name}\n"
                          f"🏟️ Visitor Team: {visitor_team_name}\n"
                          f"⚽ Over 0.5 HT: {goals05ht}%\n"
                          f"⚽ Over 1.5 HT: {entry['goals15ht']}%\n"
                          f"⚽ Over 1.5 FT: {entry['goals15ft']}%\n"
                          f"⚽ Over 2.5 FT: {entry['goals25ft']}%\n"
                          f"⚽ Over 3.5 FT: {entry['goals35ft']}%\n"
                          f"🔄 Corner Prediction: {entry['cornerprediction']}\n"
                          f"🔮 Win or Lose Market: {entry['winorlosemarket']}\n"
                          f"💰 Win or Lose Value: {entry['winorlosevalue']}\n"
                          f"🔮 BTTS Market: {entry['bttsmarket']}\n"
                          f"💰 BTTS Value: {entry['bttsvalue']}%")

                # Send the message to Telegram
                requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage", data={'chat_id': chat_id, 'text': message})

                # Add the game ID to the list of notified games
                notified_games.append(game_id)

    # Wait for an interval before checking again (e.g., every 2 minutes)
    time.sleep(120)  # 2 minutes in seconds
