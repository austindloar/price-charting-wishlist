import requests
from bs4 import BeautifulSoup
from datetime import date
from tabulate import tabulate

id_pre = "product-"
name_list = []
loose_list = []
cib_list = []
new_list = []


nnes = "https://www.pricecharting.com/console/nes"
nsnes = "https://www.pricecharting.com/console/super-nintendo"
nn64 = "https://www.pricecharting.com/console/nintendo-64"
ngc = "https://www.pricecharting.com/console/gamecube"
nwii = "https://www.pricecharting.com/console/wii"
nwiiu = "https://www.pricecharting.com/console/wii-u"
nnsw = "https://www.pricecharting.com/console/nintendo-switch"
ngb = "https://www.pricecharting.com/console/gameboy"
ngbc = "https://www.pricecharting.com/console/gameboy-color"
ngba = "https://www.pricecharting.com/console/gameboy-advance"
nnds = "https://www.pricecharting.com/console/nintendo-ds"
nds3 = "https://www.pricecharting.com/console/nintendo-3ds"
nvb = "https://www.pricecharting.com/console/virtual-boy"
ngw = "https://www.pricecharting.com/console/game-&-watch"

a2600 = "https://www.pricecharting.com/console/atari-2600"
a5200 = "https://www.pricecharting.com/console/atari-5200"
a7800 = "https://www.pricecharting.com/console/atari-7800"
a400 = "https://www.pricecharting.com/console/atari-400"
alynx = "https://www.pricecharting.com/console/atari-lynx"
ajag = "https://www.pricecharting.com/console/jaguar"

ngmvs = "https://www.pricecharting.com/console/neo-geo"
ngaes = "https://www.pricecharting.com/console/neo-geo-aes"
ngcd = "https://www.pricecharting.com/console/neo-geo-cd"
ngpc = "https://www.pricecharting.com/console/neo-geo-pocket-color"

ps1 = "https://www.pricecharting.com/console/playstation"
ps2 = "https://www.pricecharting.com/console/playstation-2"
ps3 = "https://www.pricecharting.com/console/playstation-3"
ps4 = "https://www.pricecharting.com/console/playstation-4"
ps5 = "https://www.pricecharting.com/console/playstation-5"
psp = "https://www.pricecharting.com/console/psp"
psv = "https://www.pricecharting.com/console/playstation-vita"

sms = "https://www.pricecharting.com/console/sega-master-system"
sg = "https://www.pricecharting.com/console/sega-genesis"
scd = "https://www.pricecharting.com/console/sega-cd"
s32 = "https://www.pricecharting.com/console/sega-32x"
ss = "https://www.pricecharting.com/console/sega-saturn"
sdc = "https://www.pricecharting.com/console/sega-dreamcast"
sgg = "https://www.pricecharting.com/console/sega-game-gear"
sp = "https://www.pricecharting.com/console/sega-pico"

xb = "https://www.pricecharting.com/console/xbox"
x360 = "https://www.pricecharting.com/console/xbox-360"
x1 = "https://www.pricecharting.com/console/xbox-one"
xsx = "https://www.pricecharting.com/console/xbox-series-x"

def console_request():
    global r
    bad_input = True
    while bad_input == True:    
        console = input("Which console are you looking for? (Please input it the way it is spelled in the above menu.) ")
        if console == "NES":
            r = requests.get(nnes)
            bad_input = False
        elif console == "SNES":
            r = requests.get(nsnes)
            bad_input = False
        elif console == "Nintendo 64":
            r = requests.get(nn64)
            bad_input = False
        elif console == "Gamecube":
            r = requests.get(ngc)
            bad_input = False
        elif console == "Wii":
            r = requests.get(nwii)
            bad_input = False
        elif console == "Wii U":
            r = requests.get(nwiiu)
            bad_input = False
        elif console == "Nintendo Switch":
            r = requests.get(nnsw)
            bad_input = False
        elif console == "GameBoy":
            r = requests.get(ngb)
            bad_input = False
        elif console == "GameBoy Color":
            r = requests.get(ngbc)
            bad_input = False
        elif console == "GameBoy Advance":
            r = requests.get(ngba)
            bad_input = False
        elif console == "DS":
            r = requests.get(nnds)
            bad_input = False
        elif console == "3DS":
            r = requests.get(nds3)
            bad_input = False
        elif console == "Virtual Boy":
            r = requests.get(nvb)
            bad_input = False
        elif console == "Game & Watch":
            r = requests.get(ngw)
            bad_input = False
        elif console == "2600":
            r = requests.get(a2600)
            bad_input = False
        elif console == "5200":
            r = requests.get(a5200)
            bad_input = False
        elif console == "7800":
            r = requests.get(a7800)
            bad_input = False
        elif console == "400/800":
            r = requests.get(a400)
            bad_input = False
        elif console == "Lynx":
            r = requests.get(alynx)
            bad_input = False
        elif console == "Jaguar":
            r = requests.get(ajag)
            bad_input = False
        elif console == "MVS":
            r = requests.get(ngmvs)
            bad_input = False
        elif console == "AES":
            r = requests.get(ngaes)
            bad_input = False
        elif console == "CD":
            r = requests.get(ngcd)
            bad_input = False
        elif console == "Pocket Color":
            r = requests.get(ngpc)
            bad_input = False
        elif console == "PS1":
            r = requests.get(ps1)
            bad_input = False
        elif console == "PS2":
            r = requests.get(ps2)
            bad_input = False
        elif console == "PS3":
            r = requests.get(ps3)
            bad_input = False
        elif console == "PS4":
            r = requests.get(ps4)
            bad_input = False
        elif console == "PS5":
            r = requests.get(ps5)
            bad_input = False
        elif console == "PSP":
            r = requests.get(psp)
            bad_input = False
        elif console == "PS Vita":
            r = requests.get(psv)
            bad_input = False
        elif console == "Master System":
            r = requests.get(sms)
            bad_input = False
        elif console == "Genesis":
            r = requests.get(sg)
            bad_input = False
        elif console == "32X":
            r = requests.get(s32)
            bad_input = False
        elif console == "Saturn":
            r = requests.get(ss)
            bad_input = False
        elif console == "Dreamcast":
            r = requests.get(sdc)
            bad_input = False
        elif console == "Game Gear":
            r = requests.get(sgg)
            bad_input = False
        elif console == "Pico":
            r = requests.get(sp)
            bad_input = False
        elif console == "Xbox":
            r = requests.get(xb)
            bad_input = False
        elif console == "Xbox 360":
            r = requests.get(x360)
            bad_input = False
        elif console == "Xbox One":
            r = requests.get(x1)
            bad_input = False
        elif console == "Xbox Series X":
            r = requests.get(xsx)
            bad_input = False
        else:
            print("Unknown input. Try again")
            good_input = False

def pid_request():
    global pid
    pid = input("What is the product ID of the game you have chosen? ")

def info():
    for game in game_table.find_all('tbody'):
        rows = game.find_all('tr', id=id_pre+pid)
        for row in rows:
            global name
            name = row.find('td', class_="title").text.strip()
            global price_loose
            price_loose = row.find('td', class_="used_price").text.strip()
            global price_cib
            price_cib = row.find('td', class_="cib_price").text.strip()
            global price_new
            price_new = row.find('td', class_="new_price").text.strip()

def var_entry():
    loose_no_comma = price_loose.replace(",","")
    cib_no_comma = price_cib.replace(",","")
    new_no_comma = price_new.replace(",","")

    loose_dec = loose_no_comma.strip('$')
    cib_dec = cib_no_comma.strip('$')
    new_dec = new_no_comma.strip('$')

    loose = float(loose_dec)
    cib = float(cib_dec)
    new = float(new_dec)

    name_list.append(name)
    loose_list.append(loose)
    cib_list.append(cib)
    new_list.append(new)
                        
while True:    
    print("Available Nintendo consoles:")
    print("NES")
    print("SNES")
    print("Nintendo 64")
    print("Gamecube")
    print("Wii")
    print("Wii U")
    print("Nintendo Switch")
    print("GameBoy")
    print("GameBoy Color")
    print("GameBoy Advance")
    print("DS")
    print("3DS")
    print("Virtual Boy")
    print("Game & Watch")
    print(" ")
    print("Available Atari consoles:")
    print("2600")
    print("5200")
    print("7800")
    print("400/800")
    print("Lynx")
    print("Jaguar")
    print(" ")
    print("Available Neo Geo consoles:")
    print("MVS")
    print("AES")
    print("CD")
    print("Pocket Color")
    print(" ")
    print("Available Playstation consoles:")
    print("PS1")
    print("PS2")
    print("PS3")
    print("PS4")
    print("PS5")
    print("PSP")
    print("PS Vita")
    print(" ")
    print("Available Sega consoles:")
    print("Master System")
    print("Genesis")
    print("CD")
    print("32X")
    print("Saturn")
    print("Dreamcast")
    print("Game Gear")
    print("Pico")
    print(" ")
    print("Available Xbox consoles:")
    print("Xbox")
    print("Xbox 360")
    print("Xbox One")
    print("Xbox Series X")

    console_request()
    pid_request()

    soup = BeautifulSoup(r.text, 'html.parser')
    game_table = soup.find('table', id="games_table")

    info()
    var_entry()
    
    restart = input("Would you like to add another game? (Y/N) ")
    if restart == "Y":
        continue
    elif restart == "N":
        break
    else:
        print("Unknown input. Try again")

name_list.append('Total')
loose_list.append(sum(loose_list))
cib_list.append(sum(cib_list))
new_list.append(sum(new_list))

info_t = {'Title': name_list, 'Loose Price': loose_list, 'CIB Price': cib_list, 'New Price': new_list}
print(tabulate(info_t, headers='keys', tablefmt='fancy_grid'))

k = input("Press close to exit the program.")