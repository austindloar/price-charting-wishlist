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

wishlist = input("Please enter the URL to your wishlist: ")
region = input("What region are you in? (NTSC, PAL, Japan) ")

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
        if region == "NTSC":
            url = 'https://www.pricecharting.com/search-products?q=' + name_url + '&type=prices&sort=name&console-uid=&region-name=ntsc&exclude-variants=false'
        elif region == "PAL":
            url = 'https://www.pricecharting.com/search-products?q=' + name_url + '&type=prices&sort=name&console-uid=&region-name=pal&exclude-variants=false'
        elif region == "Japan":
            url = 'https://www.pricecharting.com/search-products?q=' + name_url + '&type=prices&sort=name&console-uid=&region-name=japan&exclude-variants=false'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        global game_table
        game_table = soup.find('table', id="games_table")
        info()

def info():
    for game in game_table.find_all('tbody'):
        rows = game.find_all('tr')
        for row in rows:
            title = row.find('td', class_='title')
            name_i = title.text.strip()
            if name_i == name:
                break
            else:
                continue
        loose = title.parent.find('td', class_='used_price').text.strip()
        loose_int = loose.replace(",", "")
        loose_list.append(float(loose_int.replace("$", "")))
        cib = title.parent.find('td', class_='cib_price').text.strip()
        cib_int = cib.replace(",", "")
        cib_list.append(float(cib_int.replace("$", "")))
        new = title.parent.find('td', class_='new_price').text.strip()
        new_int = new.replace(",", "")
        new_list.append(float(new_int.replace("$", "")))
        

r = requests.get(wishlist)
soup = BeautifulSoup(r.text, 'html.parser')
wish_t = soup.find('table', id="games_table")
getWish()
search()
name_list.append("Total")
loose_list.append(sum(loose_list))
cib_list.append(sum(cib_list))
new_list.append(sum(new_list))

info_t = {'Title': name_list, 'Loose Price': loose_list, 'CIB Price': cib_list, 'New Price': new_list}
print(tabulate(info_t, headers='keys', tablefmt='fancy_grid'))

end = input("Close the program to finish. ")