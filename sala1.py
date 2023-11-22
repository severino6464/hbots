import telebot
import time
import datetime
import random

CHAVE_API = "6723085944:AAFoGwKmani3Vu_AcM3kT3VjhUSCOfFgS_E" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-5586244514'





mensagem = """
🚨 ENTRADA CONFIRMADA 🚨

🐯 Fortune Tiger 
⏰ Estratégia: Horários Pagantes
⚠️ Válido ate: {}

💰 {}x Normal
💰 {}x Turbo

⚡ Intercalando

[🔗 Fazer CADASTRO ✅](=========)
[🔗 Abrir FORTUNE TIGER](https://nuts.bet/casino/game/2180615)

"""





print("========")

 


n_jogadas = random.randint(6, 20)
n_jogadas2 = random.randint(4, 20)
validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')

time.sleep(600)  # Espera 10 minutos (600 segundos)
