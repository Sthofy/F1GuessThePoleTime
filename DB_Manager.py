import sqlite3
import datetime
import bcrypt
import dataGetter


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
    result = [row for row in curs.fetchall()]

    curs.close()
    conn.close()
    return result


def register_user(username, email, password):
    sql = "INSERT INTO User_Credentials (username, email, password) VALUES (?, ?, ?)"
    password = bcrypt.hashpw(bytes(password, encoding="utf-8"), bcrypt.gensalt())
    params = (username, email, password)
    perform_insert(sql, params)
    return True


def login_user(username):
    sql = "SELECT id,password FROM User_Credentials WHERE username=?"
    params = (username,)

    return perform_select(sql, params)


def update_user(col, data, uid):
    if col == "username":
        slq = "UPDATE User_Credentials SET username=? WHERE id=? "
        params = (data, uid)
        perform_insert(slq, params)
    elif col == "password":
        sql = "UPDATE User_Credentials SET password=? WHERE id=? "
        password = bcrypt.hashpw(bytes(data, encoding="utf-8"), bcrypt.gensalt())
        params = (password, uid)
        print(sql, params)
        perform_insert(sql, params)
    elif col == "email":
        sql = "UPDATE User_Credentials SET email=? WHERE id=? "
        params = (data, uid)
        print(sql, params)
        perform_insert(sql, params)
    elif col == "delete":
        sql = "DELETE FROM User_Credential WHERE id=?"
        params = (uid,)
        print(sql, params)
        perform_insert(sql, params)


def insert_tracks(conn, curs, data):
    sql = "INSERT INTO Tracks (location, date) VALUES (?, ?)"

    curs.execute("SELECT * FROM Tracks")
    result = curs.fetchall()

    dates = data[0]
    locations = data[1]

    if len(result) < len(dates):
        for i in range(len(dates)):
            curs.execute(sql, (locations[i], date_parser(dates[i])))
            conn.commit()


def date_parser(date):
    x = datetime.datetime.now()

    sliced = date.split()
    if sliced[0] == "március":
        return datetime.datetime(int(x.strftime("%Y")), 3, int(sliced[1][:-1]))
    elif sliced[0] == "április":
        return datetime.datetime(int(x.strftime("%Y")), 4, int(sliced[1][:-1]))
    elif sliced[0] == "május":
        return datetime.datetime(int(x.strftime("%Y")), 5, int(sliced[1][:-1]))
    elif sliced[0] == "június":
        return datetime.datetime(int(x.strftime("%Y")), 6, int(sliced[1][:-1]))
    elif sliced[0] == "július":
        return datetime.datetime(int(x.strftime("%Y")), 7, int(sliced[1][:-1]))
    elif sliced[0] == "augusztus":
        return datetime.datetime(int(x.strftime("%Y")), 8, int(sliced[1][:-1]))
    elif sliced[0] == "szeptember":
        return datetime.datetime(int(x.strftime("%Y")), 9, int(sliced[1][:-1]))
    elif sliced[0] == "október":
        return datetime.datetime(int(x.strftime("%Y")), 10, int(sliced[1][:-1]))
    elif sliced[0] == "november":
        return datetime.datetime(int(x.strftime("%Y")), 11, int(sliced[1][:-1]))
    elif sliced[0] == "december":
        return datetime.datetime(int(x.strftime("%Y")), 12, int(sliced[1][:-1]))

    return 0


def insert_team_standings(conn, curs, data):
    sql = "INSERT INTO Team_Standings (name, score) VALUES (?, ?)"
    curs.execute("DELETE FROM Team_Standings")

    pos = data[2]
    team_name = data[1]

    for i in range(len(pos)):
        curs.execute(sql, (team_name[i], pos[i]))
        conn.commit()


def insert_driver_standings(conn, curs, data):
    sql = "INSERT INTO Driver_Standings (pos, driver_name, score) VALUES (?, ?, ?)"
    curs.execute("DELETE FROM Driver_Standings")

    pos = data[0]
    driver_name = data[1]
    point = data[3]

    for i in range(len(pos)):
        curs.execute(sql, (pos[i], driver_name[i], point[i]))
        conn.commit()


def insert_drivers(conn, curs, data):
    # (driver_numbers, driver_names_long, driver_names_short, teams)
    sql = "INSERT INTO Drivers (driver_number, driver_name_long,driver_name_short, team) VALUES (?, ?, ?, ?)"
    curs.execute("SELECT * FROM Drivers")
    result = curs.fetchall()

    driver_numbers = data[0]
    driver_names_long = data[1]
    driver_names_short = data[2]
    teams = data[3]

    if len(result) < len(driver_numbers):
        for i in range(len(driver_numbers)):
            curs.execute(sql, (driver_numbers[i], driver_names_long[i], driver_names_short[i], teams[i]))
            conn.commit()


def insert_qualifications_results(conn, curs, data):
    sql = "INSERT INTO Qualification_Results (driver_id, circuit_id, time) VALUES (?, ?, ?)"
    curs.execute("SELECT * FROM Qualification_Results")
    result = curs.fetchall()
    driver_names = data[0]
    times = data[1]
    circuits = data[2]

    driver_ids = []
    circuit_ids = []

    for d in driver_names:
        driver_ids.append(get_driver_id(curs, d))

    for d in circuits:
        circuit_ids.append(get_circuit_id(d))

    if len(result) < len(times):
        for i in range(len(driver_ids)):
            curs.execute(sql, (driver_ids[i][0], circuit_ids[i][0], times[i]))
            conn.commit()


def get_driver_id(driver):
    sql = "SELECT driver_number FROM Drivers WHERE driver_name_long=?"
    output = perform_select(sql, (driver,))

    return output[0]["driver_number"]


def get_circuit_id(circuit):
    sql = "SELECT id FROM Tracks WHERE location=?"
    output = perform_select(sql, (circuit,))

    return output[0]["id"]


def load_data_from_web():
    conn = sqlite3.connect("Database/F1Guess.db")
    curs = conn.cursor()
    conn.row_factory = sqlite3.Row

    insert_tracks(conn, curs, dataGetter.get_schedule())
    insert_team_standings(conn, curs, dataGetter.get_teams_standig())
    insert_driver_standings(conn, curs, dataGetter.get_driver_standings())
    insert_drivers(conn, curs, dataGetter.get_drivers())
    insert_qualifications_results(conn, curs, dataGetter.get_qualification_results())

    curs.close()
    conn.close()


def get_all_tracks():
    conn = sqlite3.connect("Database/F1Guess.db")
    curs = conn.cursor()

    curs.execute("SELECT location,date FROM Tracks")
    out = curs.fetchall()

    curs.close()
    conn.close()
    return out


def get_driver_standings():
    conn = sqlite3.connect("Database/F1Guess.db")
    curs = conn.cursor()

    curs.execute("SELECT pos,driver_name,score FROM Driver_Standings")
    out = curs.fetchall()

    curs.close()
    conn.close()
    return out


def get_drivers_long_name():
    conn = sqlite3.connect("Database/F1Guess.db")
    curs = conn.cursor()
    conn.row_factory = sqlite3.Row

    curs.execute("SELECT driver_name_long FROM Drivers")
    out = [row[0] for row in curs.fetchall()]

    curs.close()
    conn.close()
    return out


def get_driver_name(param):
    sql = "SELECT driver_name_long FROM Drivers WHERE driver_number=?"
    out = perform_select(sql, (param,))
    return out[0]["driver_name_long"]


def get_circuit_names():
    conn = sqlite3.connect("Database/F1Guess.db")
    curs = conn.cursor()
    conn.row_factory = sqlite3.Row

    curs.execute("SELECT location FROM Tracks")
    out = [row[0] for row in curs.fetchall()]

    curs.close()
    conn.close()
    return out


def get_driver_id_from_result(param):
    c_id = get_circuit_id(param)
    sql = "SELECT driver_id FROM Qualification_Results WHERE circuit_id=?"
    out = perform_select(sql, (c_id,))

    return out[0]["driver_id"]


def insert_guess(data):
    conn = sqlite3.connect("Database/F1Guess.db")
    curs = conn.cursor()
    conn.row_factory = sqlite3.Row

    sql = "INSERT INTO User_Guess (user_id,qualification_id,user_time,driver_name) VALUES (?,?,?,?)"
    params = (data[3], get_qualification_id(curs, data[1])[0], data[2], data[0])

    curs.execute(sql, params)
    conn.commit()

    curs.close()
    conn.close()


def get_qualification_id(curs, circuit):
    curs.execute(f'SELECT id FROM Tracks WHERE location="{circuit}"')
    output = [row[0] for row in curs.fetchall()]

    return output


def get_user_score(u_id):
    sql = "SELECT score FROM User_Standings WHERE id=?"
    params = (u_id,)

    result = perform_select(sql, params)
    return result


def get_qualification_time(circuit):
    circuit_id = get_circuit_id(circuit)
    sql = "SELECT time FROM Qualification_Results WHERE circuit_id=?"
    out = perform_select(sql, (circuit_id,))[0]["time"]

    return out


def insert_user_score():
    sql = "INSERT INTO User_Standings (user_id,score) VALUES(?,?)"
