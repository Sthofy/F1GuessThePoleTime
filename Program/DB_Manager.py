import sqlite3

conn = None
curs = None


def connect():
    global conn, curs
    conn = sqlite3.connect("Database/F1Guess.db")
    curs = conn.cursor()


def close():
    if conn and curs:
        curs.close()
        conn.close()


def register_user(username, email, password, phone):
    output = False

    if ((len(username) > 0) & (len(email) > 0) & (len(password) > 0) & (len(phone) > 0)):
        try:
            curs.execute("INSERT INTO User_Credential (username, email, password, phone) VALUES (?, ?, ?, ?)", (username, email, password, phone))
            conn.commit()
            output = True
        except Exception as e:
            print(e)

    return output
