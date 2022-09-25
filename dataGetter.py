import requests
from bs4 import BeautifulSoup

url = 'https://m4sport.hu/f1-versenynaptar/?event=406'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find('div', class_='raceResultsTable practice')
p_names = {}

for pilot in table.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['line']):
    p_names[pilot.find('span', class_='pilotNameLong').text] = pilot.find('div', class_='lapTime').text

