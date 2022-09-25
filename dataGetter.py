import requests
from bs4 import BeautifulSoup


def set_soup(url):
    r = requests.get(url)
    encoding = r.encoding if 'charset' in r.headers.get('content-type', '').lower() else None
    soup = BeautifulSoup(r.content, 'html.parser', from_encoding=encoding)
    return soup


def get_tracks():
    url = 'https://m4sport.hu/f1-versenynaptar'
    soup = set_soup(url)

    tracks = {}
    table = soup.find('div', class_='F1-RaceSelectorList')
    i = 1
    for t in table.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['F1-raceUnitPlace']):
        # tracks.append(t.find('span', class_='F1-raceCountry').text)
        tracks[i] = t.find('span', class_='F1-raceCountry').text
        i += 1

    return tracks


def get_driver_standings():
    url = "https://m4sport.hu/f1-pontverseny/"
    soup = set_soup(url)

    table = soup.find('table')  # Az egész tabella
    rows = []  # Soronként az adaton <span></span> tagekben az első üres az tartalmazza a fejlécet.
    # Helyezés,Rajtszám,Teljes név,Rövidített név,Csapat teljes neve,Csapat Rövid neve,Pontszám
    pos = []
    drivers = []
    teams = []
    points = []

    for t in table.find_all('tr'):
        rows.append(t.find_all('span'))

    del rows[0]

    for p in rows:
        pos.append(p[0].text)

    for d in rows:
        drivers.append(d[2].text)

    for t in rows:
        teams.append(t[5].text)

    for dp in rows:
        points.append(dp[6].text)

    output = (pos, drivers, teams, points)

    return output


def get_schedule():
    url = "https://m4sport.hu/f1-pontverseny/"
    soup = set_soup(url)

    table = soup.find('div', class_='F1-racelist')
    dates = []
    places = []
    for r in table.find_all('div', class_='F1-raceDate'):
        dates.append(r.find('span').text)

    for p in table.find_all('div', class_='F1-racePlace'):
        places.append(p.find('span').text)
    output = (dates, places)

    return output
