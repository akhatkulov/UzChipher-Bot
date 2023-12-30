import telebot 
from telebot import types

def admin_buttons():
  key = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
  btn1 = types.KeyboardButton(text="Statistika")
  btn2 = types.KeyboardButton(text="Xabar yuborish")
  btn3 = types.KeyboardButton(text="Forward Xabar yuborish")
  key.add(btn1,btn2,btn3)
  return key

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
  btn2 = types.InlineKeyboardButton(text="➖Morze● ",callback_data="uz_morze")
  btn3 = types.InlineKeyboardButton(text="🍀Sezar",callback_data="uz_sezar")
  btn4 = types.InlineKeyboardButton(text="⚙️Hill",callback_data="uz_hill")
  key.add(btn1,btn2,btn3,btn4)
  return key

def ru_menu():
  key = types.InlineKeyboardMarkup(row_width=2)
  btn1 = types.InlineKeyboardButton(text="🌀 Мираж",callback_data="ru_mirage")
  btn2 = types.InlineKeyboardButton(text="➖Морзе●",callback_data="ru_morze")
  btn3 = types.InlineKeyboardButton(text="🍀Цезарь",callback_data="ru_sezar")
  btn4 = types.InlineKeyboardButton(text="⚙️Холм",callback_data="ru_hill")
  key.add(btn1,btn2,btn3,btn4)
  return key

def en_menu():
  key = types.InlineKeyboardMarkup(row_width=2)
  btn1 = types.InlineKeyboardButton(text="🌀Mirage",callback_data="en_mirage")
  btn2 = types.InlineKeyboardButton(text="➖Morse● ",callback_data="en_morze")
  btn3 = types.InlineKeyboardButton(text="🍀Caesar",callback_data="en_sezar")
  btn4 = types.InlineKeyboardButton(text="⚙️Hill",callback_data="en_hill")
  key.add(btn1,btn2,btn3,btn4)
  return key
###################################Uzbek Buttons############################################
def uz_mirage_mode():
  key = types.InlineKeyboardMarkup(row_width=2)
  btn1 = types.InlineKeyboardButton(text="Kodlash",callback_data="encode_mirage_uz")
  btn2 = types.InlineKeyboardButton(text="Koddan chiqarish",callback_data="decode_mirage_uz")
  key.add(btn1,btn2)
  return key
def uz_morse_mode():
  key = types.InlineKeyboardMarkup(row_width=2)
  btn1 = types.InlineKeyboardButton(text="Kodlash",callback_data="encode_morse_uz")
  btn2 = types.InlineKeyboardButton(text="Koddan chiqarish",callback_data="decode_morse_uz")
  key.add(btn1,btn2)
  return key
def uz_hill_mode():
  key = types.InlineKeyboardMarkup(row_width=2)
  btn1 = types.InlineKeyboardButton(text="Shifrlash",callback_data="encrypt_hill_uz")
  btn2 = types.InlineKeyboardButton(text="Shifrdan chiqarish",callback_data="decrypt_hill_uz")
  key.add(btn1,btn2)
  return key
def uz_sezar_mode():
  key = types.InlineKeyboardMarkup(row_width=2)
  btn1 = types.InlineKeyboardButton(text="Shifrlash",callback_data="encrypt_sezar_uz")
  btn2 = types.InlineKeyboardButton(text="Shifrdan chiqarish",callback_data="decrypt_sezar_uz")
  key.add(btn1,btn2)
  return key
#############################Russian Buttons##############################################
def ru_mirage_mode():
  key = types.InlineKeyboardMarkup(row_width=2)
  btn1 = types.InlineKeyboardButton(text="Кодирование",callback_data="encode_mirage_ru")
  btn2 = types.InlineKeyboardButton(text="Декодировать",callback_data="decode_mirage_ru")
  key.add(btn1,btn2)
  return key
def ru_morse_mode():
  key = types.InlineKeyboardMarkup(row_width=2)
  btn1 = types.InlineKeyboardButton(text="Кодирование",callback_data="encode_morse_ru")
  btn2 = types.InlineKeyboardButton(text="Декодировать",callback_data="decode_morse_ru")
  key.add(btn1,btn2)
  return key
def ru_hill_mode():
  key = types.InlineKeyboardMarkup(row_width=2)
  btn1 = types.InlineKeyboardButton(text="Шифровать",callback_data="encrypt_hill_ru")
  btn2 = types.InlineKeyboardButton(text="Расшифровать",callback_data="decrypt_hill_ru")
  key.add(btn1,btn2)
  return key
def ru_caesar_mode():
  key = types.InlineKeyboardMarkup(row_width=2)
  btn1 = types.InlineKeyboardButton(text="Шифровать", callback_data="encrypt_sezar_ru")
  btn2 = types.InlineKeyboardButton(text="Расшифровать",callback_data="decrypt_sezar_ru")
  key.add(btn1,btn2)
  return key
################################ English buttons ################################################
def en_mirage_mode():
  key = types.InlineKeyboardMarkup(row_width=2)
  btn1 = types.InlineKeyboardButton(text="Encoding",callback_data="encode_mirage_en")
  btn2 = types.InlineKeyboardButton(text="Decode",callback_data="decode_mirage_en")
  key.add(btn1,btn2)
  return key
def en_morse_mode():
  key = types.InlineKeyboardMarkup(row_width=2)
  btn1 = types.InlineKeyboardButton(text="Encoding",callback_data="encode_morse_en")
  btn2 = types.InlineKeyboardButton(text="Decode",callback_data="decode_morse_en")
  key.add(btn1,btn2)
  return key
def en_hill_mode():
  key = types.InlineKeyboardMarkup(row_width=2)
  btn1 = types.InlineKeyboardButton(text="Encrypt",callback_data="encrypt_hill_en")
  btn2 = types.InlineKeyboardButton(text="Decrypt",callback_data="decrypt_hill_en")
  key.add(btn1,btn2)
  return key
def en_sezar_mode():
  key = types.InlineKeyboardMarkup(row_width=2)
  btn1 = types.InlineKeyboardButton(text="Encrypt", callback_data="encrypt_sezar_en")
  btn2 = types.InlineKeyboardButton(text="Decrypt",callback_data="decrypt_sezar_en")
  key.add(btn1,btn2)
  return key