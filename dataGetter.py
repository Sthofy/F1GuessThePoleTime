import requests
from bs4 import BeautifulSoup


def set_soup(url):
    r = requests.get(url)
    encoding = r.encoding if 'charset' in r.headers.get('content-type', '').lower() else None
    soup = BeautifulSoup(r.content, 'html.parser', from_encoding=encoding)
    return soup


def get_driver_standings():
    rows = get_driver_related_data()
    pos = []
    drivers = []
    teams = []
    points = []

    for data in rows:
        pos.append(data[0].text)
        drivers.append(data[2].text)
        teams.append(data[5].text)
        points.append(data[6].text)

    output = (pos, drivers, teams, points)

    return output


def get_schedule():
    dates = []
    places = []
    url = "https://m4sport.hu/f1-versenynaptar/?event=361"
    soup = set_soup(url)

    table_cicuits = soup.find('div', class_='F1-RaceSelectorList')

    for t in table_cicuits.find_all("span", class_="F1-raceCity"):
        places.append(t.text)

    for t in table_cicuits.find_all("div", class_="raceDate"):
        dates.append(t.find("span").text)

    output = (dates, places)
    return output


def get_drivers():
    rows = get_driver_related_data()
    driver_numbers = []
    driver_names_long = []
    driver_names_short = []
    teams = []

    for data in rows:
        driver_numbers.append(data[1].text)
        driver_names_long.append((data[2]).text)
        driver_names_short.append(data[3].text)
        teams.append(data[5].text)

    output = (driver_numbers, driver_names_long, driver_names_short, teams)

    return output


def get_teams_standig():
    url = "https://m4sport.hu/f1-pontverseny/"
    soup = set_soup(url)

    rows = []
    pos = []
    name = []
    points = []
    table = soup.find_all('table')
    for t in table[1].find_all('tr'):
        rows.append(t.find_all('span'))

    del rows[0]

    for data in rows:
        pos.append(data[0].text)
        name.append(data[1].text)
        points.append(data[3].text)

    output = (pos, name, points)

    return output


def get_qualification_results():
    url = "https://m4sport.hu/f1-versenynaptar/?event="
    event_number = 361
    soup = set_soup(url + str(event_number))
    table = soup.find("div", class_="raceResultsTable practice")
    laptimes = []
    driver_names = []
    circuits = []

    condition = table is not None

    while condition:
        time_rows = table.find_all("div", class_="lapTime")
        laptimes.append(time_rows[1].text)
        driver_names.append(table.find("span", class_="pilotNameLong").text)
        circuits.append(get_circuit_name(soup))

        event_number += 3
        soup = set_soup(url + str(event_number))
        table = soup.find("div", class_="raceResultsTable practice")
        condition = table is not None

        if not condition:
            break

    output = (driver_names, laptimes, circuits)
    return output


def get_circuit_name(soup):
    table = soup.find("a", class_="F1-raceUnit active")
    circuit_name = table.find("span", class_="F1-raceCity").text
    return circuit_name


def get_driver_related_data():
    url = "https://m4sport.hu/f1-pontverseny/"
    soup = set_soup(url)

    table = soup.find('table')  # Az egész tabella
    output = []  # Soronként az adaton <span></span> tagekben az első üres az tartalmazza a fejlécet.
    # Helyezés,Rajtszám,Teljes név,Rövidített név,Csapat teljes neve,Csapat Rövid neve,Pontszám

    for t in table.find_all('tr'):
        output.append(t.find_all('span'))

    del output[0]  # Az üres sor törlése

    return output
