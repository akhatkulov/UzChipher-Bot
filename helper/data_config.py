import sqlite3

db = sqlite3.connect('data/database.db',check_same_thread=False,isolation_level=None)
cursor = db.cursor()

db.execute("""CREATE TABLE IF NOT EXISTS users(
    CID INT PRIMARY KEY NOT NULL,
    LANG TEXT DEFAULT "uzbek",
    STEP TEXT DEFAULT "home")""")
db.execute("""CREATE TABLE IF NOT EXISTS works(
    CID INT PRIMARY KEY NOT NULL,
    WORK TEXT
)""")


def add_step(cid,step):
    db.execute(f"UPDATE users SET step ={step} WHERE chat_id={cid}")
    db.commit()
def get_step(cid):
    x = db.cursor(f"SELECT STEP FROM users WHERE CID = {cid}")
    return x

def add_work(id,work):
    try:
        db.execute("""INSERT INTO users(CID,WORKS)
            VALUES(?,?)""",(id,work))
    except:
        pass

def get_work(id):
    x = db.cursor("""SELECT WORKS FROM works WHERE CID = ?""",(id))
    return x

def users_info():
    x = db.execute("""SELECT CID FROM users""")
    x.fetchall()
    print(x)
    return x

def add_user(cid):
    try:
        db.execute(f"INSERT INTO users(CID,STEP) VALUES({cid},'encode_mirage_uz')")
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

def get_info(id):
    x = db.cursor("""SELECT LANG FROM users WHERE CID = ?""",(id))
users_info()