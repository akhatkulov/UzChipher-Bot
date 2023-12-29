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
@bot.message_handler(chat_types=['private'])
def uz_panel(message):
    if message.text == "🇺🇿 Uzbek":
        change_lang(message.chat.id,message.text)
        bot.send_message(chat_id=message.chat.id,text="Siz o'zbek tilini tanlandingiz")
        bot.send_message(chat_id=message.chat.id,text="<b> O'zingizga kerakli shifrlash/kodlash usulini tanlang</b>",parse_mode="HTML",reply_markup=uz_menu())
    if message.text == "🇷🇺 Russian":
        change_lang(message.chat.id,message.text)
        bot.send_message(chat_id=message.chat.id,text="Вы выбрали русский")
        bot.send_message(chat_id=message.chat.id,text="<b> Выберите желаемый метод шифрования/декодирования </b>",parse_mode="HTML",reply_markup=ru_menu())
    if message.text == "🇬🇧 English":
        change_lang(message.chat.id,message.text)
        bot.send_message(chat_id=message.chat.id,text="You have selected English")
        bot.send_message(chat_id=message.chat.id,text="<b> Choose your desired encryption/decoding method</b>",parse_mode="HTML",reply_markup=en_menu())


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
    if callback.data == "ru_mirage":
        bot.send_message(chat_id=callback.message.chat.id,text="Выберите один из режимов",reply_markup=ru_mirage_mode())

    if callback.data == "ru_morze":
        bot.send_message(chat_id=callback.message.chat.id,text="Выберите один из режимов",reply_markup=ru_morse_mode())

    if callback.data == "ru_sezar":
        bot.send_message(chat_id=callback.message.chat.id,text="Выберите один из режимов",reply_markup=ru_caesar_mode())

    if callback.data == "ru_hill":
        bot.send_message(chat_id=callback.message.chat.id,text="Выберите один из режимов",reply_markup=ru_hill_mode())
    
    if callback.data == "encode_mirage_ru":
        bot.send_message(chat_id=callback.message.chat.id,text=f"Отправьте текст, который вы хотите закодировать")
        add_step(callback.message.chat.id,"encode_mirage_ru")

    if callback.data == "decode_mirage_ru":
        bot.send_message(chat_id=callback.message.chat.id,text="Отправьте текст, который хотите расшифровать")
        add_step(callback.message.chat.id,"decode_mirage_ru")
    
    if callback.data == "encode_morse_ru":
        bot.send_message(chat_id=callback.message.chat.id,text="Отправьте текст, который вы хотите закодировать")
        add_step(callback.message.chat.id,"encode_morse_ru")
    if callback.data == "decode_morse_ru":
        bot.send_message(chat_id=callback.message.chat.id,text="Отправьте текст, который хотите расшифровать")
        add_step(callback.message.chat.id,"encode_morse_ru")

    if callback.data == "encrypt_hill_ru":
        bot.send_message(chat_id=callback.message.chat.id,text="Отправьте текст, который вы хотите зашифровать")
        add_step(callback.message.chat.id,"encrypt_hill_ru")
    if callback.data == "decrypt_hill_ru":
        bot.send_message(chat_id=callback.message.chat.id,text="Отправьте текст, который хотите расшифровать")
        add_step(callback.message.chat.id,"decrypt_hill_ru")
    
    if callback.data == "encrypt_sezar_ru":
        bot.send_message(chat_id=callback.message.chat.id,text="Отправьте текст, который хотите расшифровать")
        add_step(callback.message.chat.id,"encrypt_sezar_ru")
    if callback.data == "decrypt_sezar_ru":
        bot.send_message(chat_id=callback.message.chat.id,text="Отправьте текст, который хотите расшифровать")
        add_step(callback.message.chat.id,"decrypt_sezar_ru")
    if callback.data == "en_mirage":
        bot.send_message(chat_id=callback.message.chat.id,text="Choose one of the modes",reply_markup=en_mirage_mode())

    if callback.data == "en_morze":
        bot.send_message(chat_id=callback.message.chat.id,text="Choose one of the modes",reply_markup=en_morse_mode())

    if callback.data == "en_sezar":
        bot.send_message(chat_id=callback.message.chat.id,text="Choose one of the modes",reply_markup=en_sezar_mode())

    if callback.data == "en_hill":
        bot.send_message(chat_id=callback.message.chat.id,text="Choose one of the modes",reply_markup=en_hill_mode())

@bot.message_handler()
def uz_panel(message):
    step = get_step(message.chat.id)
    if step == "home":
        pluser()
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
        if "Error"!=hillEncrypt(get_work1(message.chat.id),message.text):
            bot.send_message(chat_id=message.chat.id,text=f"<b>Asl matn: </b><code>{get_work1(message.chat.id)}</code>\n<b>Parol: </b><code>{message.text}</code>\n<b>Natija: </b><code>{hillEncrypt(get_work1(message.chat.id),message.text)} </code>",parse_mode="HTML")
            add_step(message.chat.id,"home")
        else:
            bot.send_message(chat_id=message.chat.id,text="Siz xatoga yo'l qo'ydingiz. Botdan qanday foydalanish haqida tanishib chiqing! /help -- ushbu buyruqni yuboring!")

    if step == "decrypt_hill_uz":
        add_work1(message.chat.id,message.text)
        bot.send_message(chat_id=message.chat.id,text="Parolingizni yuboring",parse_mode="HTML")
        add_step(message.chat.id,"hill_de_uz")
    if step == "hill_de_uz":
        if "Error"!=hillDecrypt(get_work1(message.chat.id),message.text):
            bot.send_message(chat_id=message.chat.id,text=f"<b>Shifrlangan matn: </b><code>{get_work1(message.chat.id)}</code>\n<b>Parol: </b><code>{message.text}</code>\n<b>Natija: </b><code>{hillDecrypt(get_work1(message.chat.id),message.text)} </code>",parse_mode="HTML")
            add_step(message.chat.id,"home")
        else:
            bot.send_message(chat_id=message.chat.id,text="Siz xatoga yo'l qo'ydingiz. Botdan qanday foydalanish haqida tanishib chiqing! /help -- ushbu buyruqni yuboring!")

    if step == "encrypt_sezar_uz":
        add_work1(message.chat.id,message.text)
        bot.send_message(chat_id=message.chat.id,text="1dan 27gacha bo'lgan raqamlardan birni kiriting. Masalan: 17",parse_mode="HTML")
        add_step(message.chat.id,"sezar_2_uz")
    if step == "sezar_2_uz":
        if "Error"!=caesar_encipher(get_work1(message.chat.id),message.text):
            bot.send_message(chat_id=message.chat.id,text=f"<b>Asl matn: </b><code>{get_work1(message.chat.id)}</code>\n<b>Parol: </b><code>{message.text}</code>\n<b>Natija: </b><code>{caesar_encipher(get_work1(message.chat.id),message.text)} </code>",parse_mode="HTML")
            add_step(message.chat.id,"home")
        else:
            bot.send_message(chat_id=message.chat.id,text="Siz xatoga yo'l qo'ydingiz. Botdan qanday foydalanish haqida tanishib chiqing! /help -- ushbu buyruqni yuboring!")

    if step == "decrypt_sezar_uz":
        add_work1(message.chat.id,message.text)
        bot.send_message(chat_id=message.chat.id,text="1dan 27gacha bo'lgan sonlardan birini yuboring",parse_mode="HTML")
        add_step(message.chat.id,"sezar_de_uz")
      
    if step == "sezar_de_uz":
        if "Error" != caesar_decipher(get_work1(message.chat.id),message.text):
            bot.send_message(chat_id=message.chat.id,text=f"<b>Shifrlangan matn: </b><code>{get_work1(message.chat.id)}</code>\n<b>Parol: </b><code>{message.text}</code>\n<b>Natija: </b><code>{caesar_decipher(get_work1(message.chat.id),message.text)} </code>",parse_mode="HTML")
            add_step(message.chat.id,"home")
        else:
            bot.send_message(chat_id=message.chat.id,text="Siz xatoga yo'l qo'ydingiz. Botdan qanday foydalanish haqida tanishib chiqing! /help -- ushbu buyruqni yuboring!")
##################################### Russian Section ###########################################
    if step == "home_ru":
         pluser()
    if step=="encode_mirage_ru":
        bot.send_message(chat_id=message.chat.id,text=f"<b>Ваш текст успешно закодирован \n\n</b> <b>Исходный текст: </b> <code>{message.text}</code> \n<b>Закодированный текст: </b >< code>{en_mirage(message.text)}</code>",parse_mode="HTML")
        add_step(message.chat.id,"home_ru")
    if step=="decode_mirage_ru":
        bot.send_message(chat_id=message.chat.id,text=f"<b>Ваш текст успешно декодирован \n\n</b><b>Закодированный текст: </b><code>{message.text}</code>\n<b>Результат: </b> <code>{de_mirage(message.text)}</code>",parse_mode="HTML")
        add_step(message.chat.id,"home_ru")
    if step=="encode_morse_ru":
        bot.send_message(chat_id=message.chat.id,text=f"<b>Ваш текст успешно закодирован \n\n</b> <b>Исходный текст: </b> <code>{message.text}</code> \n<b>Закодированный текст: </b >< code>{text_to_morse(message.text)}</code>",parse_mode="HTML")
        add_step(message.chat.id,"home_ru")
    if step=="decode_morse_ru":
        bot.send_message(chat_id=message.chat.id,text=f"<b>Ваш текст успешно декодирован \n\n</b><b>Закодированный текст: </b><code>{message.text}</code>\n<b>Результат: </b> <code>{morse_to_text(message.text)}</code></code>",parse_mode="HTML")
        add_step(message.chat.id,"home_ru")

    if step == "encrypt_hill_ru":
        add_work1(message.chat.id,message.text)
        bot.send_message(chat_id=message.chat.id,text="Отправьте свой пароль",parse_mode="HTML")
        add_step(message.chat.id,"hill_2_ru")
    if step == "hill_2_ru":
        if "Error"!=hillEncrypt(get_work1(message.chat.id),message.text):
            bot.send_message(chat_id=message.chat.id,text=f"<b>Исходный текст: </b><code>{get_work1(message.chat.id)}</code>\n<b>Пароль: </b><code>{message.text}</code> \n<b>Результат: </b><code>{hillEncrypt(get_work1(message.chat.id),message.text)} </code>",parse_mode="HTML")
            add_step(message.chat.id,"home_ru")
        else:
            bot.send_message(chat_id=message.chat.id,text="Вы сделали ошибку. Научитесь пользоваться ботом! /help — отправьте эту команду!")

    if step == "decrypt_hill_ru":
        add_work1(message.chat.id,message.text)
        bot.send_message(chat_id=message.chat.id,text="Отправьте свой пароль",parse_mode="HTML")
        add_step(message.chat.id,"hill_de_ru")
    if step == "hill_de_ru":
        if "Error"!=hillDecrypt(get_work1(message.chat.id),message.text):
            bot.send_message(chat_id=message.chat.id,text=f"<b>Зашифрованный текст: </b><code>{get_work1(message.chat.id)}</code>\n<b>Пароль: </b><code>{message.text}</code> \n<b>Результат: </b><code>{hillDecrypt(get_work1(message.chat.id),message.text)} </code>",parse_mode="HTML")
            add_step(message.chat.id,"home_ru")
        else:
            bot.send_message(chat_id=message.chat.id,text="Вы сделали ошибку. Научитесь пользоваться ботом! /help — отправьте эту команду!")

    if step == "encrypt_sezar_ru":
        add_work1(message.chat.id,message.text)
        bot.send_message(chat_id=message.chat.id,text="Введите одну из цифр от 1 до 27. Например: 17",parse_mode="HTML")
        add_step(message.chat.id,"sezar_2_ru")
    if step == "sezar_2_ru":
        if "Error"!=caesar_encipher(get_work1(message.chat.id),message.text):
            bot.send_message(chat_id=message.chat.id,text=f"<b>Исходный текст: </b><code>{get_work1(message.chat.id)}</code>\n<b>Пароль: </b><code>{message.text}</code> \n<b>Результат: </b><code>{caesar_encipher(get_work1(message.chat.id),message.text)} </code>",parse_mode="HTML")
            add_step(message.chat.id,"home_ru")
        else:
            bot.send_message(chat_id=message.chat.id,text="Вы сделали ошибку. Научитесь пользоваться ботом! /help — отправьте эту команду!")

    if step == "decrypt_sezar_ru":
        add_work1(message.chat.id,message.text)
        bot.send_message(chat_id=message.chat.id,text="Отправьте одно из чисел от 1 до 27.",parse_mode="HTML")
        add_step(message.chat.id,"sezar_de_ru")
      
    if step == "sezar_de_ru":
        if "Error" != caesar_decipher(get_work1(message.chat.id),message.text):
            bot.send_message(chat_id=message.chat.id,text=f"<b>Зашифрованный текст: </b><code>{get_work1(message.chat.id)}</code>\n<b>Пароль: </b><code>{message.text}</code> \n<b>Результат: </b><code>{caesar_decipher(get_work1(message.chat.id),message.text)} </code>",parse_mode="HTML")
            add_step(message.chat.id,"home_ru")
        else:
            bot.send_message(chat_id=message.chat.id,text="Вы сделали ошибку. Научитесь пользоваться ботом! /help — отправьте эту команду!")
################################### English Section ####################################################################

    if step == "home_en":
        pluser()
    if step=="encode_mirage_en":
        bot.send_message(chat_id=message.chat.id,text=f"<b>Your text has been successfully encoded \n\n</b> <b>Original Text: </b> <code>{message.text}< /code> \n<b>Encoded text: </b><code>{en_mirage(message.text)}</code>",parse_mode="HTML")
        add_step(message.chat.id,"home_en")
    if step=="decode_mirage_en":
        bot.send_message(chat_id=message.chat.id,text=f"<b>Your text has been decoded successfully \n\n</b><b>Encoded text: </b><code>{message.text} </code>\n<b>Result: </b><code>{de_mirage(message.text)}</code>",parse_mode="HTML")
        add_step(message.chat.id,"home_en")
    if step=="encode_morse_en":
        bot.send_message(chat_id=message.chat.id,text=f"<b>Your text has been successfully encoded \n\n</b> <b>Original Text: </b> <code>{message.text}< /code> \n<b>Encoded text: </b><code>{text_to_morse(message.text)}</code>",parse_mode="HTML")
        add_step(message.chat.id,"home_en")
    if step=="decode_morse_en":
        bot.send_message(chat_id=message.chat.id,text=f"<b>Your text has been decoded successfully \n\n</b><b>Encoded text: </b><code>{message.text} </code>\n<b>Result: </b><code>{morse_to_text(message.text)}</code>",parse_mode="HTML")
        add_step(message.chat.id,"home_en")
    if step == "encrypt_hill_uz":
        add_work1(message.chat.id,message.text)
        bot.send_message(chat_id=message.chat.id,text="Send your password",parse_mode="HTML")
        add_step(message.chat.id,"hill_2_uz")
    if step == "hill_2_en":
        if "Error"!=hillEncrypt(get_work1(message.chat.id),message.text):
                bot.send_message(chat_id=message.chat.id,text=f"<b>Original text: </b><code>{get_work1(message.chat.id)}</code>\n<b>Password: </b><code>{message.text}</code>\n<b>Result: </b><code>{hillEncrypt(get_work1(message.chat.id),message.text)} </code >",parse_mode="HTML")
                add_step(message.chat.id,"home_en")
        else:
            bot.send_message(chat_id=message.chat.id,text="You made an error. Learn how to use the bot! /help -- send this command!")

    if step == "decrypt_hill_en":
        add_work1(message.chat.id,message.text)
        bot.send_message(chat_id=message.chat.id,text="Send your password",parse_mode="HTML")
        add_step(message.chat.id,"hill_de_en")
    if step == "hill_de_en":
        if "Error"!=hillDecrypt(get_work1(message.chat.id),message.text):
            bot.send_message(chat_id=message.chat.id,text=f"<b>Encrypted text: </b><code>{get_work1(message.chat.id)}</code>\n<b>Password: </b><code>{message.text}</code>\n<b>Result: </b><code>{hillDecrypt(get_work1(message.chat.id),message.text)} </code >",parse_mode="HTML")
            add_step(message.chat.id,"home_en")
        else:
            bot.send_message(chat_id=message.chat.id,text="You made an error. Learn how to use the bot! /help -- send this command!")
    if step == "encrypt_sezar_en":
        add_work1(message.chat.id,message.text)
        bot.send_message(chat_id=message.chat.id,text="Enter a number from 1 to 27. For example: 17",parse_mode="HTML")
        add_step(message.chat.id,"sezar_2_en")
    if step == "sezar_2_en":
        if "Error"!=caesar_encipher(get_work1(message.chat.id),message.text):
            bot.send_message(chat_id=message.chat.id,text=f"<b>Original text: </b><code>{get_work1(message.chat.id)}</code>\n<b>Password: </b><code>{message.text}</code>\n<b>Result: </b><code>{caesar_encipher(get_work1(message.chat.id),message.text)} </code >",parse_mode="HTML")
            add_step(message.chat.id,"home_en")
        else:
            bot.send_message(chat_id=message.chat.id,text="You made an error. Learn how to use the bot! /help -- send this command!")

    if step == "decrypt_sezar_en":
        add_work1(message.chat.id,message.text)
        bot.send_message(chat_id=message.chat.id,text="Send one of the numbers from 1 to 27",parse_mode="HTML")
        add_step(message.chat.id,"sezar_de_en")
      
    if step == "sezar_de_uz":
        if "Error" != caesar_decipher(get_work1(message.chat.id),message.text):
            bot.send_message(chat_id=message.chat.id,text=f"<b>Encrypted text: </b><code>{get_work1(message.chat.id)}</code>\n<b>Password: </b><code>{message.text}</code>\n<b>Result: </b><code>{caesar_decipher(get_work1(message.chat.id),message.text)} </code >",parse_mode="HTML")
            add_step(message.chat.id,"home_en")
        else:
            bot.send_message(chat_id=message.chat.id,text="You made an error. Learn how to use the bot! /help -- send this command!")
bot.polling()   