import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
def getodds(season, week):
    url = 'https://fantasydata.com/nfl-stats/point-spreads-and-odds?season={}&seasontype=1&week={}'\
            .format(season,week)
    data = urlopen(url)
    soup = BeautifulSoup(data,"lxml")
    for tr in soup.find_all('tr'):
        tds = tr.find_all('td')
        print(tds)
season1 = getodds(2010,1)