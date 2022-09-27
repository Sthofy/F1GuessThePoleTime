from datetime import timedelta

import DB_Manager

CORRECT_DRIVER = 500
logged_in_user_id = -1


def load_previous_score(u_id):
    score = DB_Manager.get_user_score(u_id)
    if score:
        return score
    else:
        return 0


def load_correct_time(circuit):
    c_time = DB_Manager.get_qualification_time(circuit)
    return c_time


def load_correct_driver(circuit):
    d_id = DB_Manager.get_driver_id_from_result(circuit)
    c_driver = DB_Manager.get_driver_name(d_id)
    return c_driver


guess_data = ["Max Verstappen", "Szahír", " 1:30.558", 1]


def timeConvert(param):
    d = timedelta(minutes=int(param[0:2]), seconds=int(param[3:5]), microseconds=int(param[6:9] + "000"))
    return d


def calculate_score(guess_data):
    # guess = (driver, circuit, time, self.logged_in_user)
    p_score = load_previous_score(guess_data[3])
    correct_time = load_correct_time(guess_data[1])
    correct_driver = load_correct_driver(guess_data[1])
    user_time = guess_data[2]
    user_driver = guess_data[0]

    c_time = timeConvert(correct_time)
    print(c_time)
    u_time = timeConvert(user_time)
    if c_time < u_time:
        diff = u_time - c_time
        print(diff.microseconds)
    elif c_time > u_time:
        diff = c_time - u_time
        print(diff.microseconds)
    else:
        print("Zero")


calculate_score(guess_data)
