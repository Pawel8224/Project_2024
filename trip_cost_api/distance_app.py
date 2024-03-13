import tkinter as tk
import psycopg2
import requests
from tkinter import *
import webbrowser
from requests import get
from tkinter import messagebox, Entry
from os import environ
from dotenv import load_dotenv
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

data = psycopg2.connect(dbname="trip_cost", host="mws02.mikr.us", port="50189", user="postgres", password="x8nfNgNnDm")

root = Tk()
root.configure(bg='black', bd=0)
root.title('Plan Your Trip')
root.geometry('490x830+400+100')
root.resizable(width=False, height=False)

origins = ""
destinations = ""


##########################################################################################################
# --------------------------------------------- METHODS --------------------------------------------------#

def delete_trip():
    result = messagebox.askyesno(title='Delete trip', message='Are you sure you want to delete trip?')
    if result:
        cur = data.cursor()
        cur.execute("""DELETE FROM travel""")
        data.commit()
        window.destroy()
    else:
        pass


def export_list():
    cur = data.cursor()
    cur.execute("""SELECT travel,distance,duration, cost FROM travel""")
    result = cur.fetchall()

    e_list = list(sum(result, ()))

    with open('travel_list_new', 'w') as f:
        for line in e_list:
            f.write(line)
            f.write('\n')


def show_trip():
    cur = data.cursor()
    cur.execute("""SELECT travel, distance, duration, cost FROM travel""")
    result = cur.fetchall()

    for row in result:
        y = (str('Travel:'))
        z = (str(row[0]))
        x = (str(row[1]))
        v = (str(row[2]))
        m = (str(row[3]))
        doc = ''
        sumtrip_list.insert(END, y)
        sumtrip_list.insert(END, z)
        sumtrip_list.insert(END, x)
        sumtrip_list.insert(END, v)
        sumtrip_list.insert(END, m)
        sumtrip_list.insert(END, doc)


def msg_savebut():
    messagebox.showinfo(title='Information', message="Your travel has been saved!")


def msg_exportbut():
    messagebox.showinfo(title="Information", message="Export list done")


def New_Window():
    global window
    window = tk.Toplevel()
    window.configure(background='white')
    window.resizable(width=False, height=False)
    window.geometry('400x500')

    canvas2 = tk.Canvas(window, width=400, height=500)
    canvas2.pack(fill='both', expand=True)
    canvas2.pack()

    canvas2.create_text(195, 30, text='YOUR TRIP', font='calibri 20', fill='white')

    ### BUTTON - wyczysc

    Button(window, text='Delete Trip List', font='calibri 15', fg='black', bd=0, bg='black',
           command=lambda: [delete_trip(), show_trip()]).place(x=40, y=70)

    ### BUTTON - export do txt

    Button(window, text='Export Travel', font='calibri 15', fg='black', bg='white', bd=0,
           command=lambda: [export_list(), msg_exportbut()]).place(x=220, y=69)

    ### OKNO - WYNIK

    global sumtrip_list
    frame_sumtrip = Frame(window, width=300, height=300, bd=0, bg='white')
    frame_sumtrip.place(x=40, y=120)

    sumtrip_list = Listbox(frame_sumtrip, font=('arial', 14), width=40, height=19, bg='#e4eaf5', fg='black')
    sumtrip_list.pack(side=LEFT, fill=BOTH, padx=2)


def openURL():
    # otwiera URL do Google Maps

    if origins is None:
        webbrowser.open('https://www.google.pl/maps/preview')
    else:
        webbrowser.open(f'https://www.google.pl/maps/dir/{origins}/{destinations}')


def openGasURL():
    webbrowser.open('https://cena-paliw.pl/')


def clearList():
    # czysci liste

    sumary_list.delete(0, END)


def checkerror():
    # wyświetla błąd

    if statusi == 'NOT_FOUND':
        messagebox.showwarning(title='Information', message='City not found! \n Check the data provided')
    else:
        print('')


def summary():
    # podsumowanie

    load_dotenv()
    api_key = environ.get('API_KEY')
    global origins
    global destinations
    global statusi

    origins = addres_entryO.get()
    destinations = addres_entryD.get()
    gas = int(float(gas_entry.get()))
    price = int(float(price_entry.get()))
    tollBut = toll_button.get()
    highBut = high_button.get()

    # wywołujemy URL do API
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"

    # podajemy dane dot. trasy

    pay_load = {
        'origins': f'{origins}',
        'destinations': f'{destinations}',
        'key': api_key,
        'avoid': f'{tollBut}',
        'avoid': f'{highBut}'

    }

    # wywołujemy jsona
    response = get(url, pay_load)
    body = response.json()
    print(body)

    statusi = body['rows'][0]['elements'][0]['status']
    checkerror()
    distance = body['rows'][0]['elements'][0]['distance']
    duration = body['rows'][0]['elements'][0]['duration']

    distance2 = distance['text']
    duration2 = duration['text']

    cost = price * distance['value'] / 1000 * gas / 100
    cost2 = round(cost, 2)

    global a
    global b
    global c
    global d
    global doc

    doc = f'{origins} - {destinations}'
    a = f'Droga do pokonania: {distance2}'
    b = f'Czas przejazdu {duration2}'
    c = f'Koszt przejazdu: {cost2} PLN'
    d = f''

    sumary_list.insert(END, doc)
    sumary_list.insert(END, a)
    sumary_list.insert(END, b)
    sumary_list.insert(END, c)
    sumary_list.insert(END, d)


def d_weather(city):
    # zaciąga dane z API Pogodowego

    load_dotenv()
    api_keyW = environ.get('API_KEYW')
    urlW = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

    global country
    global citys
    global temp_cel
    global icon
    global weathers

    result = requests.get(urlW.format(city, api_keyW))

    if result:
        json = result.json()
        citys = json['name']
        country = json['sys']['country']
        temp_kel = json['main']['temp']
        temp_cel = temp_kel - 273.15
        weathers = json['weather'][0]['main']
        icon = json['weather'][0]['icon']
        final = (city, country, temp_cel, icon, weathers)
        print(final)
    else:
        return None


def show_weather():
    # wyświetlanie pogody

    city = addres_entryD.get()
    weather = d_weather(city)

    location_lbl['text'] = '{}, {}'.format(country, citys)
    weather_image['bitmap'] = 'icon/{}.png'.format(icon)
    temp_lbl['text'] = '{:.2f}℃'.format(temp_cel)
    weather_lbl['text'] = '{}'.format(weathers)


## SQLITE - zapis/odczyt

def create_table(data):
    try:
        cur = data.cursor()
        sql = "CREATE TABLE IF NOT EXISTS travel(travel TEXT, distance TEXT, duration TEXT, cost TEXT)"
        cur.execute(sql)
        data.commit()
    except psycopg2.Error as e:
        print(e)


def save_trip():
    try:
        print(doc, a, b, c)
    except:
        messagebox.showwarning(title="Information", message="Your save travel is empty!")

    cur = data.cursor()
    cur.execute("""
                INSERT INTO travel(travel, distance, duration, cost)
                VALUES(%s,%s,%s,%s) 
                """, (doc, a, b, c))

    data.commit()


############################### ---  OKNO GLOWNE  ---  #######################################################
# ---------------------------------  FRONTEND ---------------------------------------------------------------#
create_table(data)

canvas1 = Canvas(root, width=490, height=830)
canvas1.pack(fill='both', expand=True)

# BACKGROUND

bb = PhotoImage(file='/Users/pablom/PycharmProjects/Projekty2024/trip_cost_api/bbg.png')
canvas1.create_image(0, 68, image=bb, anchor="nw")

# TOPBAR
TopImage = PhotoImage(file='/Users/pablom/PycharmProjects/Pliki/distance_app/ab.png')
canvas1.create_image(0, 0, image=TopImage, anchor="nw")

# IKONA GOOGLE MAPS - OTWIERA LINK  ------------------------------------------------
dockImage = PhotoImage(file='/Users/pablom/PycharmProjects/Pliki/distance_app/top_icon.png')
Button(root, image=dockImage, bd=0, bg='grey', command=openURL).place(x=40, y=95)

# IKONA PALIWA
gasImage = PhotoImage(file='/Users/pablom/PycharmProjects/Pliki/distance_app/gas.png')
Button(root, image=gasImage, bd=0, bg='black', command=openGasURL).place(x=110, y=95)

# TEKST GŁÓWNY ------------------------------------------------

canvas1.create_text(300, 115, text="Plan your trip!", font='calibri 25 bold', fill='black')

##############################  ---- OKNA ---  ##############################

# OKNO START PODROZY  ------------------------------------------------
frameO = Frame(root, width=190, height=35, bg='grey')
frameO.place(x=180, y=190)

addres_entryO = Entry(frameO, width=14, font='calibri 20', bd=0, bg='#e4eaf5', fg='black')
addres_entryO.place(x=0, y=1)

canvas1.create_text(110, 208, text="ORIGIN", font='calibri 18 bold', fill='black', )

# OKNO - KONIEC PODROZY  ------------------------------------------------
frameD = Frame(root, width=190, height=35, bg='grey')
frameD.place(x=180, y=240)

addres_entryD = Entry(frameD, width=14, font='calibri 20', bd=0, bg='#e4eaf5', fg='black')
addres_entryD.place(x=0, y=1)

canvas1.create_text(109, 258, text="DESTINATION", font='calibri 17 bold', fill='black')

# OKNO - SPALANIE  ------------------------------------------------

frameS = Frame(root, width=86, height=35, bg='grey')
frameS.place(x=180, y=299)

gas_entry = Entry(frameS, width=6, font='calibri 20', bd=0, bg='#e4eaf5', fg='black')
gas_entry.place(x=0, y=1)

canvas1.create_text(107, 316, text="FUEL USAGE", font='calibri 17 bold', fill='black')

# OKNO - CENA PALIWA ------------------------------------------------

frameP = Frame(root, width=86, height=35, bg='grey')
frameP.place(x=180, y=354)

price_entry = Entry(frameP, width=6, font='calibri 20', bd=0, bg='#e4eaf5', fg='black')
price_entry.place(x=0, y=1)

canvas1.create_text(108, 372, text="FUEL PRICE", font='calibri 17 bold', fill='black')

###########################------- CHECKBOX  ----##############################

# CHECKBOX - ODCINKI PLATNE ----------------------------------------------------------------
toll_button = StringVar()
tolbutton = Checkbutton(root, width=2, onvalue='tolls', offvalue='none', variable=toll_button).place(x=180, y=406)

canvas1.create_text(110, 417, text='Toll roads', font='calibri 17', fill='black')

# CHECKBOX - AUTOSTRADY ----------------------------------------------------------------

high_button = StringVar()
high_tbutton = Checkbutton(root, width=2, onvalue='highways', offvalue='none', variable=high_button).place(x=180, y=435)

canvas1.create_text(110, 450, text='Highways', font='calibri 17', fill='black')

############################### ---- BUTTON ----- ##############################


# BUTTON - POKAZ WYNIK / WYCZYSC ------------------------------------------------

summary_button = Button(root, text='TIME / DISTANCE / COST', font='calibri 15', fg='black', bd=0, bg='white',
                        command=lambda: [summary(), show_weather()])
summary_button.place(x=145, y=480)

d_button = Button(root, text='CLEAR', font='calibri 15', fg='black', bd=0, bg='white', command=clearList)
d_button.place(x=200, y=512)

# BUTTON - ZAPISZE DANE / ODTWORZ / POKAZ PODROZE -------------------------------------------------

savetrip = Button(root, text='Save\nTrip', font='calibri 13', fg='black',
                  command=lambda: [save_trip(), msg_savebut()]).place(x=8, y=560)

open_trip = Button(root, text='Show\nTrip', font='calibri 13', fg='black',
                   command=lambda: [New_Window(), show_trip()]).place(x=7, y=625)

############################### ---- WYNIK DANE ----- ##############################


# LISTBOX - RAMKA Z WYNIKIEM ------------------------------------------------
frame_summary = Frame(root, width=290, height=150, bd=0, bg='grey')
frame_summary.place(x=90, y=550)

sumary_list = Listbox(frame_summary, font=('arial', 18), width=29, height=6, bg='#e4eaf5', fg='black')
sumary_list.pack(side=LEFT, fill=BOTH, padx=2)

############################### ---- POGODA  ----- ##############################

location_lbl = Label(root, text='', font='calibri 21')
location_lbl.place(x=140, y=690)

weather_image = Label(root, bitmap='')
weather_image.place(x=290, y=700)

temp_lbl = Label(root, text='', font='calibri 19')
temp_lbl.place(x=140, y=740)

weather_lbl = Label(root, text='', font='calibri 19')
weather_lbl.place(x=140, y=770)

root.mainloop()
