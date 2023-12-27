import telebot 
from telebot import types
from helper import *
from cipher_codes import *


if get_step(message.chat.id)=="encode_mirage_uz":
    x = en_mirage(message.text)
    bot.send_message(chat_id=message.chat.id,text=f"<b>Sizning matningiz muvaffaqiyatli kodlandi</b> <br><code>{x}</code>",parse_mode="HTML")
    uz_panel()