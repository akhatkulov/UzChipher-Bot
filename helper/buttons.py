import telebot 
from telebot import types


def lang_button():
  lang = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
  uz = types.KeyboardButton(text="🇺🇿 Uzbek")
  ru = types.KeyboardButton(text="🇷🇺 Russian")
  en = types.KeyboardButton(text="🇬🇧 English")
  lang.add(uz,ru,en)
  return lang


def uz_menu():
  key = types.InlineKeyboardMarkup(row_width=2)
  btn1 = types.InlineKeyboardButton(text="🌀Mirage",callback_data="uz_mirage")
  btn1 = types.InlineKeyboardButton(text="➖Morze● ",callback_data="uz_morze")
  btn1 = types.InlineKeyboardButton(text="🍀Sezar",callback_data="uz_sezar")
  btn1 = types.InlineKeyboardButton(text="🌀Mirage",callback_data="uz_hill")


