import requests
from bs4 import BeautifulSoup


def pyconjp():
    url = 'https://pycon.jp/2017/ja/sponsors/'
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    sponsors = soup.find_all('div', class_='sponsor-content')
    for sponsor in sponsors:
        url = sponsor.h3.a['href']
        name = sponsor.h4.text
        print(name, url)


def bivican():
    url = 'https://www.bivicam.jp/news_event/'
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    dls = soup.find_all('dl', class_='clearfix')
    for dl in dls:
        date = dl.dt.text
        text = dl.dd.a.text
        print(date, text)


def bivican2():
    url = 'https://www.bivicam.jp/news_event/'
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    dls = soup.find_all('dl', class_='clearfix')
    for dl in dls:
        date = dl.dt.text
        dd = dl.dd
        a = dd.find('a')
        if a:
            print(date, a.text)
        else:
            print(date, dd.text)


def cookpad():
    url = "https://cookpad.com"
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    sponsored = soup.find('div', class_='sponsored_kitchen_ads')
    lis = sponsored.ul.find_all('li', class_='clearfix')
    for li in lis:
        anchor = li.div.find('a', class_='recipe_title')
        print(anchor.text)


def satv_am():
    url = "https://www.satv.co.jp/0200weekly/"
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    time_table = soup.find('div', class_='timeTable am')
    rows = time_table.find_all('tr')
    for row in rows:
        print(row.th.text, row.td.text)


def satv():
    url = "https://www.satv.co.jp/0200weekly/"
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    time_tables = soup.find_all('div', class_='timeTable')
    for time_table in time_tables:
        rows = time_table.find_all('tr')
        for row in rows:
            print(row.th.text, row.td.text)


if __name__ == '__main__':
   # pyconjp()
    bivican()
    # bivican2()
    # cookpad()
    # satv()