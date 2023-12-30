import sqlite3

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


def n_append(id,lang):
    db.execute("""INSERT INTO users(CID,LANG)
        VALUES(?,?)""",(id,lang))
    db.commit()

def change_lang(cid,lang):
    db.execute("""UPDATE users SET lang=? WHERE cid =?""",(lang,cid))
    db.commit()

def get_lang(cid):
    x = db.cursor("""SELECT LANG FROM users WHERE CID = ?""",(cid))
    return x