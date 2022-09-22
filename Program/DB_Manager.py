import sqlite3
import Models.LoggedInUserModel as LoggedInUserModel

conn = None
curs = None


def open_connection():
    global conn, curs
    conn = sqlite3.connect("Database/F1Guess.db")
    curs = conn.cursor()


def close_connection():
    if conn and curs:
        curs.close()
        conn.close()


def register_user(username, email, password, phone):
    output = False

    if (len(username) > 0) & (len(email) > 0) & (len(password) > 0) & (len(phone) > 0):
        try:
            open_connection()

            curs.execute("INSERT INTO User_Credential (username, email, password, phone) VALUES (?, ?, ?, ?)",
                         (username, email, password, phone))
            conn.commit()

            close_connection()

            output = True
        except Exception as e:
            print(e)

    return output


def login_user(username, password):
    try:
        line = []
        open_connection()

        curs.execute(f'''SELECT * FROM User_Credential WHERE username="{username}" AND password="{password}"''')
        datas = curs.fetchall()

        close_connection()

        for data in datas:
            line = data

        LoggedInUserModel.uid = line[0]
        LoggedInUserModel.username = line[1]
        LoggedInUserModel.email = line[2]
        LoggedInUserModel.password = line[3]
        LoggedInUserModel.phone = line[4]

    except Exception as e:
        print(e)

    return LoggedInUserModel
