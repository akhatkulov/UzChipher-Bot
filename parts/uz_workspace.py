import telebot 
from telebot import types
from helper import *
from cipher_codes import *

bot = telebot.TeleBot("6482725249:AAEG6jO6tCYQEVfbPeKxkQv1RgPwvJ896q0")

@bot.message_handler(content_types=['text'])
def chipher_uz(message):
    if get_step(message.chat.id)=="encode_mirage_uz":
        x = en_mirage(message.text)
        bot.send_message(chat_id=message.chat.id,text=f"<b>Sizning matningiz muvaffaqiyatli kodlandi</b> <br><code>{x}</code>",parse_mode="HTML")
        uz_panel()
