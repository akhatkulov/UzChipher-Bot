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
    bot.send_message(chat_id=message.chat.id,text="<b> O'zingizga kerakli shifrlash/kodlash usulini tanlang</b>",parse_mode="HTML")
@bot.callback_query_handler(func= lambda callback : callback.data)
def uz_inline():
    if callback.data == "uz_mirage":
        bot.send_message(chat_id=callback.data.chat.id,text="Kodlamoqchi bo'lgan matningizni yuboring")
        add_step(callback.data.chat.id,"uz_mirage")
    if callback.data == "uz_morze":
        bot.send_message(chat_id=callback.data.chat.id,text="Kodlamoqchi bo'lgan matningizni yuboring")
        add_step(callback.data.chat.id,"uz_morze")
    if callback.data == "uz_sezar":
        bot.send_message(chat_id=callback.data.chat.id,text="Shifrlamoqchi bo'lgan matningizni yuboring")
        add_step(callback.data.chat.id,"uz_sezar")
    if callback.data == "uz_hill":
        bot.send_message(chat_id=callback.data.chat.id,text="Shifrlamoqchi bo'lgan matningizni yuboring")
        add_step(callback.data.chat.id,"uz_hill")


##################################### Russian Section ###########################################

@bot.message_handler(chat_types=['private'],func= lambda x : x.text == "🇷🇺 Russian")
def ru_panel(message):
    change_lang(message.chat.id,message.text)
    bot.send_message(chat_id=message.chat.id,text="Вы выбрали русский")
    bot.send_message(chat_id=message.chat.id,text="<b> Выберите желаемый метод шифрования/декодирования </b>",parse_mode="HTML")
################################### English Section ####################################################################
@bot.message_handler(chat_types=['private'],func= lambda x : x.text == "🇬🇧 English")
def en_panel(message):
    change_lang(message.chat.id,message.text)
    bot.send_message(chat_id=message.chat.id,text="You have selected English")
    bot.send_message(chat_id=message.chat.id,text="<b> Choose your desired encryption/decoding method</b>",parse_mode="HTML")

bot.polling()   