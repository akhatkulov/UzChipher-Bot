import sqlite3

db = sqlite3.connect('data/database.db')
cursor = db.cursor()

db.execute("""CREATE TABLE IF NOT EXISTS users(
    CID INT PRIMARY KEY NOT NULL,
    STAT INT NOT NULL,
    CHANNEL TEXT NOT NULL
)""")

