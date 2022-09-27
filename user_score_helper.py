from datetime import timedelta

import DB_Manager

CORRECT_DRIVER = 500
MAX_SCORE = 1000


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


def time_convert(param):
    d = timedelta(minutes=int(param[0:2]), seconds=int(param[3:5]), microseconds=int(param[6:9] + "000"))
    return d


def calculate_score(guess_data):
    # guess = (driver, circuit, time, self.logged_in_user)
    score = load_previous_score(guess_data[3])
    correct_time = load_correct_time(guess_data[1])
    correct_driver = load_correct_driver(guess_data[1])
    user_time = guess_data[2]
    user_driver = guess_data[0]

    c_time = time_convert(correct_time)
    u_time = time_convert(user_time)
    if c_time < u_time:  # + ág
        diff = u_time - c_time
        if diff.seconds > 0:
            score += 0
        else:
            score += (1000 - int(str(diff.microseconds)[0:3]))

    elif c_time > u_time:  # - ág
        diff = c_time - u_time
        if diff.seconds > 0:
            score += 0
        else:
            score += (1000 - int(str(diff.microseconds)[0:3]))
    else:
        score += MAX_SCORE

    if correct_driver == user_driver:
        score += CORRECT_DRIVER

    return score
