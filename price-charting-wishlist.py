from os import name
from types import NoneType
import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from tabulate import tabulate

id_pre = 'product-' #BS4 has trouble with concatenated arguments
name_list = []
loose_list = []
cib_list = []
new_list = []
name_url_list = []
today = date.today()
now = datetime.now().strftime('%I:%M:%S %p')
datentime = str(today) + ' ' + str(now)

wishlist = input('Please enter the URL to your wishlist: ')
if wishlist != 'admin': #Makes it easier for dev to access his list
    region = input('What region are you in? (NTSC, PAL, Japan) ') #Different regions have different prices; Planning support for wishlists with games of varying regions
else:
    wishlist = 'https://www.pricecharting.com/wishlist?user=co4xkx425noxuatk7fvazrenn4' #Dev's list and region
    region = 'NTSC'

def getWish(): #Parses through list to get names of all games in list
    for game in wish_t.find_all('tr'):
        datas = game.find_all('td')
        for data in datas:
            as_ = data.find_all('a')
            for a_ in as_:
                name = a_.text.strip()
                name_url = a_.text.strip().replace(' ', '+') #Formats it for queries in the search URL
                name_list.append(name)
                name_url_list.append(name_url)

def search(): #Basically runs through each name in the array and puts it into search URL (q=game+name)
    for i in range(len(name_list)):
        global name_url
        name_url = name_list[i]
        global name
        name = name_list[i].replace('+', ' ') #Appends name without + to list (prolly a better way to do this)
        if region == 'NTSC':
            url = 'https://www.pricecharting.com/search-products?q=' + name_url + '&type=prices&sort=name&console-uid=&region-name=ntsc&exclude-variants=false'
        elif region == 'PAL':
            url = 'https://www.pricecharting.com/search-products?q=' + name_url + '&type=prices&sort=name&console-uid=&region-name=pal&exclude-variants=false'
        elif region == 'Japan':
            url = 'https://www.pricecharting.com/search-products?q=' + name_url + '&type=prices&sort=name&console-uid=&region-name=japan&exclude-variants=false'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        global game_table
        game_table = soup.find('table', id='games_table')
        info()

def info(): #Parses through HTML of given search URL for all three prices
    for game in game_table.find_all('tbody'):
        rows = game.find_all('tr')
        for row in rows:
            title = row.find('td', class_='title')
            if type(title) == NoneType:
                continue
            name_i = title.text.strip()
            if name_i == name:
                break
            else:
                continue
        loose = title.parent.find('td', class_='used_price').text.strip() #Should make this into separate function but I don't feel like it
        loose_int = loose.replace(',', '') #Removes dollar sign and any commas to prepare for type conversion to float
        loose_list.append(float(loose_int.replace('$', '')))
        cib = title.parent.find('td', class_='cib_price').text.strip()
        cib_int = cib.replace(',', '')
        cib_list.append(float(cib_int.replace('$', '')))
        new = title.parent.find('td', class_='new_price').text.strip()
        new_int = new.replace(',', '')
        new_list.append(float(new_int.replace('$', '')))
        

r = requests.get(wishlist)
soup = BeautifulSoup(r.text, 'html.parser')
wish_t = soup.find('table', id='games_table')

getWish()
search()

name_list.append('Total')
loose_list.append(sum(loose_list))
cib_list.append(sum(cib_list))
new_list.append(sum(new_list))

info_t = {'Title': name_list, 'Loose Price': loose_list, 'CIB Price': cib_list, 'New Price': new_list} #Dictionary for use of tabulate

output = str(today) + ' ' + str(now) + '\n' + tabulate(info_t, headers='keys', tablefmt='fancy_grid')
print(output)

worse_output = str(today) + ' ' + str(now) + '\n' + tabulate(info_t, headers='keys', tablefmt='grid') #Need this because it can't write certain character to text file from better output
yn = input('Write table to text file? (Y/N) ')
if yn == 'Y':
    with open('wishlist-' + str(today) + '.txt', 'w') as f:
        f.write(worse_output)
        print('Text file saved in same location as EXE')
end = input('Close the program to finish. ') #Would be a shame if the program closed before you could see the result >:)