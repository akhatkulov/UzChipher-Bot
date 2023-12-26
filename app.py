import telebot
from helper import *
bot = telebot.TeleBot("6482725249:AAEG6jO6tCYQEVfbPeKxkQv1RgPwvJ896q0")

@bot.message_handler(commands=['start'])

def home(message):
    bot.send_message(chat_id=message.chat.id, text=f"👋Choose your language👇",reply_markup=lang_button())

@bot.message_handler(chat_types=['private'],func= lambda x : x.text == "🇺🇿 Uzbek")
def uz_panel(message):
    bot.send_message(chat_id=message.chat.id,text="Siz o'zbek tilini tanlandingiz")
    bot.send_message(chat_id=message.chat.id,text="<b> O'zingizga kerakli menyuni tanlang</b>",parse_mode="HTML")
    n_append(message.chat.id,"uzbek")

@bot.message_handler(commands=['lang'])
def changer_lang():
    bot.send_message(chat_id=message.chat.id, text=f"👋Choose your language👇",reply_markup=lang_button())
    
bot.polling()   