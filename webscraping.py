import json
import pandas as pd
import requests
from datetime import datetime, timedelta
import time

# Define your Telegram bot token and chat ID
bot_token = "SEU_BOT_TOKEN"
chat_id = "SEU_CHATID"  # Substitua pelo ID do seu canal

# Lista para rastrear os jogos que já foram notificados
notified_games = []

# Loop continuamente com um intervalo de verificação (por exemplo, a cada 2 minutos)
while True:
    # Lê o arquivo JSON
    with open('/content/partidas-22-08.json') as f:
        data = json.load(f)

    # Fuso horário original (+3)
    original_timezone = timedelta(hours=3)

    for entry in data['data']:
        game_id = entry['id']  # Obtém o ID do jogo
        if game_id in notified_games:
            continue  # Pula o jogo se já foi notificado

        goals05ht = entry['goals05ht']  # Obtém o valor de goals05ht
        goals15ht = entry['goals15ht']  # Obtém o valor de goals15ht
        if goals05ht >= 80 and goals15ht >= 60:  # Verifica as condições
            home_team_name = entry['localTeam']['name']
            visitor_team_name = entry['visitorTeam']['name']
            match_datetime = datetime.strptime(entry['starting_time'], "%Y-%m-%d %H:%M:%S")
            adjusted_match_datetime = match_datetime - original_timezone

            # Calcula a diferença de tempo até o início do jogo (10 minutos)
            time_until_match = (match_datetime - datetime.now()).total_seconds()
            time_to_send = 10 * 60  # 10 minutos em segundos

            if 0 <= time_until_match <= time_to_send:
                # Obtém o nome da liga do jogo
                league_name = entry['league_name']

                # Formata a mensagem para enviar ao Telegram
                message = ("🔔 NOVA OPORTUNIDADE DE OVER 0.5 HT PRESTES A INICIAR\n\n"
                          f"📰 Fonte dos dados: SokkerPro\n"
                          f"🏆 Liga: {league_name}\n"
                          f"⏰ Hora: {adjusted_match_datetime.time()}\n"
                          f"🏠 Time da Casa: {home_team_name}\n"
                          f"🏟️ Time Visitante: {visitor_team_name}\n"
                          f"⚽ Over 0.5 HT: {goals05ht}%\n"
                          f"⚽ Over 1.5 HT: {entry['goals15ht']}%\n"
                          f"⚽ Over 1.5 FT: {entry['goals15ft']}%\n"
                          f"⚽ Over 2.5 FT: {entry['goals25ft']}%\n"
                          f"⚽ Over 3.5 FT: {entry['goals35ft']}%\n"
                          f"🔄 Previsão de Escanteios: {entry['cornerprediction']}\n"
                          f"🔮 Win or Lose Market: {entry['winorlosemarket']}\n"
                          f"💰 Win or Lose Value: {entry['winorlosevalue']}\n"
                          f"🔮 BTTS Market: {entry['bttsmarket']}\n"
                          f"💰 BTTS Value: {entry['bttsvalue']}%")

                # Envia a mensagem ao Telegram
                requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage", data={'chat_id': chat_id, 'text': message})

                # Adiciona o ID do jogo à lista de jogos notificados
                notified_games.append(game_id)

    # Aguarda por um intervalo antes de verificar novamente (por exemplo, a cada 2 minutos)
    time.sleep(120)  # 2 minutos em segundos
