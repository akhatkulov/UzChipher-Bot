import telebot 
from telebot.types import *

def main_key():
  key = InlineKeyboardMarkup(row_width=1)
  key.add(
    InlineKeyboardButton('Mirage',callback_data='photo'),
    InlineKeyboardButton('📝 Text to Audio',callback_data='tts_menu'),
  )
  return key