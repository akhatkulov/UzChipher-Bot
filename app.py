from telebot import *

bot = TeleBot(token="6482725249:AAEG6jO6tCYQEVfbPeKxkQv1RgPwvJ896q0")

@bot.message_handler(commands='start')
def home(msg: types.Message):
    bot.send_message(msg.from_user.id,"""👋 Salom  botimizga xush kelibsiz!

🔰 Quyidagi menyular orqali botdan foydalaning 👇""")
    

bot.infinity_polling()