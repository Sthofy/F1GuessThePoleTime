import sqlite3
import bcrypt


def perform_insert(sql, params):
    conn = sqlite3.connect("Database/F1Guess.db")
    curs = conn.cursor()

    curs.execute(sql, params)
    conn.commit()

    curs.close()
    conn.close()


def perform_select(sql, params):
    conn = sqlite3.connect("Database/F1Guess.db")
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    curs.execute(sql, params)
    result = [dict(row) for row in curs.fetchall()]

    curs.close()
    conn.close()
    return result


def register_user(username, email, password, phone):
    sql = "INSERT INTO User_Credential (username, email, password, phone) VALUES (?, ?, ?, ?)"
    password = bcrypt.hashpw(bytes(password, encoding="utf-8"), bcrypt.gensalt())
    params = (username, email, password, phone)
    perform_insert(sql, params)
    return True


def login_user(username):
    sql = "SELECT password FROM User_Credential WHERE username=?"
    params = (username,)

    return perform_select(sql, params)


def update_user(col, data, uid):
    if col == "username":
        slq = "UPDATE User_Credential SET username=? WHERE id=? "
        params = (data, uid)
        perform_insert(slq, params)
    elif col == "password":
        sql = "UPDATE User_Credential SET password=? WHERE id=? "
        password = bcrypt.hashpw(bytes(data, encoding="utf-8"), bcrypt.gensalt())
        params = (password, uid)
        print(sql, params)
        # perform_insert(slq, params)
    elif col == "email":
        sql = "UPDATE User_Credential SET email=? WHERE id=? "
        params = (data, uid)
        print(sql, params)
        perform_insert(sql, params)
    elif col == "phone":
        sql = "UPDATE User_Credential SET phone=? WHERE id=? "
        params = (data, uid)
        print(sql, params)
        perform_insert(sql, params)
    elif col == "delete":
        sql = "DELETE FROM User_Credential WHERE id=?"
        params = (uid,)
        print(sql, params)
        perform_insert(sql, params)
