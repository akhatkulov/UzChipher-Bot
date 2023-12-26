import telebot
from helper import *
bot = telebot.TeleBot("6482725249:AAEG6jO6tCYQEVfbPeKxkQv1RgPwvJ896q0")

@bot.message_handler(commands=['start'])
def home(message):
    bot.send_message(message.chat.id,f"""👋 Salom {str(message.from_user.first_name)}  botimizga xush kelibsiz!

🔰 Quyidagi menyular orqali botdan foydalaning 👇""")
    

bot.polling() 