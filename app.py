import telebot

bot = telebot.TeleBot("YOUR_BOT_TOKEN",parse_mode='html')

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "<b> Howdy, how are you doing? <b> ")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()