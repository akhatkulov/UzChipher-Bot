import telebot 
from telebot import types


def lang_button():
  lang = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
  uz = types.KeyboardButton(text="🇺🇿 Uzbek")
  ru = types.KeyboardButton(text="🇷🇺 Russian")
  en = types.KeyboardButton(text="🇬🇧 English")
  lang.add(uz,ru,en)
  return lang

