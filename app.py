import time
import telebot
from helper import *
from cipher_codes import *
bot = telebot.TeleBot("6482725249:AAEG6jO6tCYQEVfbPeKxkQv1RgPwvJ896q0")

@bot.message_handler(commands=['start','lang'])
def home(message):
    bot.send_message(chat_id=message.chat.id, text=f"👋Choose your language👇",reply_markup=lang_button())
    add_user(message.chat.id)


##################################### Uzbek Section #####################################
@bot.message_handler(chat_types=['private'],func= lambda x : x.text == "🇺🇿 Uzbek")
def uz_panel(message):
    change_lang(message.chat.id,message.text)
    bot.send_message(chat_id=message.chat.id,text="Siz o'zbek tilini tanlandingiz")
    bot.send_message(chat_id=message.chat.id,text="<b> O'zingizga kerakli shifrlash/kodlash usulini tanlang</b>",parse_mode="HTML",reply_markup=uz_menu())

@bot.callback_query_handler(func= lambda callback : callback.data)
def uz_inline(callback):
    if callback.data == "uz_mirage":
        bot.send_message(chat_id=callback.message.chat.id,text="Rejimlardan birini tanlang",reply_markup=uz_mirage_mode())

    if callback.data == "uz_morze":
        bot.send_message(chat_id=callback.message.chat.id,text="Rejimlardan birini tanlang",reply_markup=uz_morse_mode())

    if callback.data == "uz_sezar":
        bot.send_message(chat_id=callback.message.chat.id,text="Rejimlardan birini tanlang",reply_markup=uz_sezar_mode())

    if callback.data == "uz_hill":
        bot.send_message(chat_id=callback.message.chat.id,text="Rejimlardan birini tanlang",reply_markup=uz_hill_mode())
    
    
    if callback.data == "encode_mirage_uz":
        bot.send_message(chat_id=callback.message.chat.id,text=f"Kodlamoqchi bo'lgan matningizni yuboring")
        add_step(callback.message.chat.id,"encode_mirage_uz")

    if callback.data == "decode_mirage_uz":
        bot.send_message(chat_id=callback.message.chat.id,text="Koddan chiqarmoqchi bo'lgan matningizni yuboring")
        add_step(callback.message.chat.id,"decode_mirage_uz")
    
    if callback.data == "encode_morse_uz":
        bot.send_message(chat_id=callback.message.chat.id,text="Kodlamoqchi bo'lgan matningizni yuboring")
        add_step(callback.message.chat.id,"encode_morse_uz")
    if callback.data == "decode_morse_uz":
        bot.send_message(chat_id=callback.message.chat.id,text="Koddan chiqarmoqchi bo'lgan matningizni yuboring")
        add_step(callback.message.chat.id,"encode_morse_uz")

    if callback.data == "encrypt_hill_uz":
        bot.send_message(chat_id=callback.message.chat.id,text="Shifrlamoqchi bo'lgan matningizni yuboring")
        add_step(callback.message.chat.id,"encrypt_hill_uz")
    if callback.data == "decrypt_hill_uz":
        bot.send_message(chat_id=callback.message.chat.id,text="Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
        add_step(callback.message.chat.id,"decrypt_hill_uz")
    
    if callback.data == "encrypt_sezar_uz":
        bot.send_message(chat_id=callback.message.chat.id,text="Shifrlamoqchi bo'lgan matningizni yuboring")
        add_step(callback.message.chat.id,"encrypt_sezar_uz")
    if callback.data == "decrypt_sezar_uz":
        bot.send_message(chat_id=callback.message.chat.id,text="Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
        add_step(callback.message.chat.id,"decrypt_sezar_uz")

@bot.message_handler()
def uz_panel(message):
    step = get_step(message.chat.id)
    if step == "home":
        time.sleep(3)
        bot.send_message(chat_id=message.chat.id,text="<b> O'zingizga kerakli shifrlash/kodlash usulini tanlang</b>",parse_mode="HTML",reply_markup=uz_menu())
    if step=="encode_mirage_uz":
        bot.send_message(chat_id=message.chat.id,text=f"<b>Sizning matningiz muvaffaqiyatli kodlandi \n\n</b> <b>Asl Matn: </b> <code>{message.text}</code> \n<b>Kodlangan matn: </b><code>{en_mirage(message.text)}</code>",parse_mode="HTML")
        add_step(message.chat.id,"home")
    if step=="decode_mirage_uz":
        bot.send_message(chat_id=message.chat.id,text=f"<b>Sizning matningiz muvaffaqiyatli koddan chiqarildi \n\n</b><b>Kodlangan matn: </b><code>{message.text}</code>\n<b>Natija: </b><code>{de_mirage(message.text)}</code>",parse_mode="HTML")
        add_step(message.chat.id,"home")
    if step=="encode_morse_uz":
        bot.send_message(chat_id=message.chat.id,text=f"<b>Sizning matningiz muvaffaqiyatli kodlandi \n\n</b> <b>Asl Matn: </b> <code>{message.text}</code> \n<b>Kodlangan matn: </b><code>{text_to_morse(message.text)}</code>",parse_mode="HTML")
        add_step(message.chat.id,"home")
    if step=="decode_morse_uz":
        bot.send_message(chat_id=message.chat.id,text=f"<b>Sizning matningiz muvaffaqiyatli koddan chiqarildi \n\n</b><b>Kodlangan matn: </b><code>{message.text}</code>\n<b>Natija: </b><code>{morse_to_text(message.text)}</code>",parse_mode="HTML")
        add_step(message.chat.id,"home")
    if step == "encrypt_hill_uz":
        add_work1(message.chat.id,message.text)
        bot.send_message(chat_id=message.chat.id,text="Parolingizni yuboring",parse_mode="HTML")
        add_step(message.chat.id,"hill_2_uz")
    if step == "hill_2_uz":
        bot.send_message(chat_id=message.chat.id,text=f"{get_work1(message.chat.id)} {hillEncrypt(get_work1(message.chat.id),message.text)}")
        add_step(message.chat.id,"home")
##################################### Russian Section ###########################################

@bot.message_handler(chat_types=['private'],func= lambda x : x.text == "🇷🇺 Russian")
def ru_panel(message):
    change_lang(message.chat.id,message.text)
    bot.send_message(chat_id=message.chat.id,text="Вы выбрали русский")
    bot.send_message(chat_id=message.chat.id,text="<b> Выберите желаемый метод шифрования/декодирования </b>",parse_mode="HTML",reply_markup=ru_menu())
@bot.callback_query_handler(func= lambda callback : callback.data)
def ru_inline(callback):
    if callback.data == "ru_mirage":
        bot.send_message(chat_id=callback.message.chat.id,text="Выберите один из режимов",reply_markup=ru_mirage_mode())

    if callback.data == "ru_morze":
        bot.send_message(chat_id=callback.data.chat.id,text="Выберите один из режимов",reply_markup=ru_morse_mode())

    if callback.data == "ru_sezar":
        bot.send_message(chat_id=callback.message.chat.id,text="Выберите один из режимов",reply_markup=ru_caesar_mode())

    if callback.data == "ru_hill":
        bot.send_message(chat_id=callback.message.chat.id,text="Выберите один из режимов",reply_markup=ru_hill_mode())

################################### English Section ####################################################################
@bot.message_handler(chat_types=['private'],func= lambda x : x.text == "🇬🇧 English")
def en_panel(message):
    change_lang(message.chat.id,message.text)
    bot.send_message(chat_id=message.chat.id,text="You have selected English")
    bot.send_message(chat_id=message.chat.id,text="<b> Choose your desired encryption/decoding method</b>",parse_mode="HTML",reply_markup=en_menu())
@bot.callback_query_handler(func= lambda callback : callback.data)
def en_inline(callback):
    if callback.data == "en_mirage":
        bot.send_message(chat_id=callback.message.chat.id,text="Choose one of the modes",reply_markup=en_mirage_mode())

    if callback.data == "en_morze":
        bot.send_message(chat_id=callback.data.chat.id,text="Choose one of the modes",reply_markup=en_morse_mode())

    if callback.data == "en_sezar":
        bot.send_message(chat_id=callback.message.chat.id,text="Choose one of the modes",reply_markup=en_sezar_mode())

    if callback.data == "en_hill":
        bot.send_message(chat_id=callback.message.chat.id,text="Choose one of the modes",reply_markup=en_hill_mode())


bot.polling()   