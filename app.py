import telebot

bot = telebot.TeleBot("6482725249:AAEG6jO6tCYQEVfbPeKxkQv1RgPwvJ896q0")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, """👋 Salom The Wind 卍 | 🇺🇿AC botimizga xush kelibsiz!

🔰 Quyidagi menyular orqali botdan foydalaning 👇""")

bot.infinity_polling()