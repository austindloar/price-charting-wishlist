from os import name
import requests
from bs4 import BeautifulSoup
from datetime import date
from tabulate import tabulate

id_pre = "product-"
name_list = []
loose_list = []
cib_list = []
new_list = []
name_url_list = []

wishlist = "https://www.pricecharting.com/wishlist?user=co4xkx425noxuatk7fvazrenn4"

def getWish():
    for game in wish_t.find_all('tr'):
        datas = game.find_all('td')
        for data in datas:
            as_ = data.find_all('a')
            for a_ in as_:
                name = a_.text.strip()
                name_url = a_.text.strip().replace(" ", "+")
                name_list.append(name)
                name_url_list.append(name_url)

def search():
    for i in range(len(name_list)):
        global name_url
        name_url = name_list[i]
        global name
        name = name_list[i].replace("+", " ")
        url = "https://www.pricecharting.com/search-products?console-uid=&exclude-variants=false&q=" + name_url + "&region-name=ntsc&sort=name&type=prices&broad-category=video-games"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        global game_table
        game_table = soup.find('table', id="games_table")
        info()

def info():
    for game in game_table.find_all('tbody'):
        rows = game.find_all('tr')
        for row in rows:
            data = row.find('td', class_='title')
            name_i = data.text.strip()
            if name_i == name:
                break
            else:
                continue



r = requests.get(wishlist)
soup = BeautifulSoup(r.text, 'html.parser')
wish_t = soup.find('table', id="games_table")
getWish()
search()