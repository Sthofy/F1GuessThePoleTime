import sqlite3

# Létrehozás(ha nem létezik) és kapcsolódás
conn = sqlite3.connect("Database/F1Guess.db")
curs = conn.cursor()

conn.close()
