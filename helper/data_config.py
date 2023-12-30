import sqlite3
import telebot

bot = telebot.TeleBot("6482725249:AAEG6jO6tCYQEVfbPeKxkQv1RgPwvJ896q0")
admin_id = 789945598

db = sqlite3.connect('data/database.db',check_same_thread=False,isolation_level=None)
cursor = db.cursor()

db.execute("""CREATE TABLE IF NOT EXISTS users(
    CID INT UNIQUE NOT NULL,
    LANG TEXT DEFAULT "uzbek",
    WORK1 TEXT DEFAULT "none",
    WOKR2 TEXT DEFAULT "none",
    STEP TEXT DEFAULT "home")""")
db.execute("CREATE TABLE IF NOT EXISTS stat(ID INTIGER UNIQUE DEFAULT 1, WORK INTIGER DEFAULT 1)")

def pluser():
    # x = db.execute("SELECT * FROM stat WHERE id=1")
    # x=int()
    # x+=1
    # db.execute("UPDATE stat SET work=? WHERE id=1",(x))
    print("--[]--")

def add_step(cid,step):
    db.execute(f"UPDATE users SET step=? WHERE cid=?",(str(step),int(cid)))
    print("--{}--")
    db.commit()
def get_step(cid):
    x = db.execute(f"SELECT * FROM users WHERE cid={cid}")
    return x.fetchone()[4]
    print("++++")

def add_work1(cid,work):
    db.execute(f"UPDATE users SET work1=? WHERE cid=?",(str(work),int(cid)))
    db.commit()
def get_work1(cid):
    x = cursor.execute(f"SELECT * FROM users WHERE cid={cid}")
    return x.fetchone()[2]
def add_work2(cid,work):
    db.execute(f"UPDATE users SET work2={work} WHERE cid={cid}")
    db.commit()
def get_work2(cid):
    x = cursor.execute(f"SELECT * FROM users WHERE cid={cid}")
    return x.fetchone()[3]

def add_user(cid):
    try:
        db.execute(f"INSERT INTO users(CID) VALUES({cid})")
    except:
        pass
    db.commit()

def ads_send(message):
    try:
        text = message.text
        if text=="🚫 Bekor qilish":
            bot.send_photo(message.chat.id,photo="https://t.me/the_solodest/178",caption="🚫 Xabar yuborish bekor qilindi !")
        else:
            cursor.execute("SELECT cid FROM users")
            rows = cursor.fetchall()
            for i in rows:
                chat_id = i[0]
                print(chat_id)
                bot.send_message(chat_id,message.text)
            bot.send_photo(admin_id,photo="https://t.me/the_solodest/178",caption="<b>✅ Xabar hamma foydalanuvchiga yuborildi!</b>")
    except:
        pass
def get_stat():
    cursor.execute("SELECT COUNT(CID) FROM users")
    rows = cursor.fetchall()
    return rows[0][0]
def for_send(message):
    text = message.text
    if text == "🚫 Bekor qilish":
        bot.send_photo(message.chat.id,photo="https://t.me/the_solodest/178",caption="🚫 Xabar yuborish bekor qilindi!")
    else:
        cursor.execute("SELECT cid FROM users")
        rows = cursor.fetchall()
        for row in rows:
            try:
                chat_id = row[0]
                print(chat_id)
                bot.forward_message(chat_id, admin_id, message.message_id)
            except Exception as e:
                print(e)
        bot.send_message(admin_id, "✅ Xabar hamma foydalanuvchiga yuborildi!")

def change_lang(cid,lang):
    db.execute("""UPDATE users SET lang=? WHERE cid =?""",(lang,cid))
    db.commit()

def get_lang(cid):
    x = db.cursor("""SELECT LANG FROM users WHERE CID = ?""",(cid))
    return x