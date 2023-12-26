import sqlite3

db = sqlite3.connect('data/database.db',check_same_thread=False)
cursor = db.cursor()

db.execute("""CREATE TABLE IF NOT EXISTS users(
    CID INT PRIMARY KEY NOT NULL,
    LANG TEXT DEFAULT "uzbek",
    STEP TEXT DEFAULT "home")""")

def users_info():
    x = db.execute("""SELECT CID FROM users""")
    x.fetchall()
    print(x)
    return x

def add_user(cid):
    try:
        db.execute("""INSERT INTO users(CID)
            VALUES(?,?)""",(cid))
    except:
        pass
    db.commit()


def n_append(id,lang):
    db.execute("""INSERT INTO users(CID,LANG)
        VALUES(?,?)""",(id,lang))
    db.commit()

def change_lang(id,lang):
    db.execute("""UPDATE users set LANG = ? WHERE CID = ?""",(lang,id))
    db.commit()
def add_step(id,step):
    db.execute("""UPDATE users set STEP = ? WHERE CID = ?""",(id,step))
    db.commit()
def get_step(id):
    x = db.cursor("""SELECT STEP FROM users WHERE CID = ?""",(id))
    return x
def get_info(id):
    x = db.cursor("""SELECT LANG FROM users WHERE CID = ?""",(id))
users_info()