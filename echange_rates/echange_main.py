from tkinter import *
import tkinter as tk
import requests
from tkinter import messagebox

#############  DEF   #############

def act_rate():
    global aft_value
    aft_currency = option_var.get()
    body = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/')
    response = body.json()

    try:
        aft_value = float(ammount.get())
        for rate in response[0]['rates']:
            if rate['code'] == aft_currency:
                currency_new = str(rate['code'])
                value_new = float(rate['mid'])
                sum = '%.2f' % (aft_value / float(value_new))
        Label(root, text='Waluta: ' + currency_new, font='calibri 20').place(x=90, y=230)
        Label(root, text='Kurs: ' + str(value_new), font='calibri 20').place(x=90, y=270, )
        Label(root, text='Otrzymasz: ' + sum, font='calibri 20').place(x=90, y=310)
    except:
        messagebox.showinfo(title='Informacja', message='Nie podałeś wartości KWOTA')


def sum_history_value():
    url_date = date_entry.get()

    try:
        url = "http://api.nbp.pl/api/exchangerates/tables/A/%s/" % (str(url_date))
        body1 = requests.get(url)
        response1 = body1.json()
        frame_show_cur = Frame(new_windows, width=60, height=30, bd=0, bg='white')
        frame_show_cur.place(x=20, y=80)

        show_cur = Listbox(frame_show_cur, font=('calibri', 14), width=40, height=28, bg='#e4eaf5', fg='black')
        show_cur.pack(side=LEFT, fill=BOTH)

        for rate1 in response1[0]['rates']:
            cur = str(rate1['currency'])
            cod = str(rate1['code'])
            val = float(rate1['mid'])

            text_sum = " %s | %s | Kurs: %s" % (cod, cur, float(val))
            show_cur.insert(END, text_sum)
    except:
        messagebox.showwarning(title='Komunikat', message='Nie ma takiej daty w bazie')


def new_window_history():
    global new_windows
    global date_entry
    new_windows = tk.Toplevel()
    new_windows.title('Przelicznik kursów walut')
    new_windows.geometry('400x600')
    new_windows.resizable(width=False, height=False)

    Label(new_windows, text='Kursy historyczne', font='calibri 17 bold').place(x=120, y=5)
    Label(new_windows, text='ROK-MIESIAC-DZIEN: ', font='calibri 13').place(x=10, y=45)
    Button(new_windows, text='Pokaż wyniki', font='calibri 13', fg='black', bg='white',
           command=sum_history_value).place(x=270, y=41)

    date = StringVar()
    date_entry = Entry(new_windows, textvariable=date, width=10, font='calibri 14', fg='white', bd=0, bg='grey')
    date_entry.place(x=160, y=45)


############# TKINTER  #############

root = Tk()
root.title('Przelicznik kursów walut')
root.geometry('400x500')
root.resizable(width=False, height=False)

canvas = Canvas(root, width=600, height=600)
canvas.pack(fill='both')

bg_photo = PhotoImage(file='/Users/pablom/PycharmProjects/Projekty2024/echange_rates/bbg.png')
canvas.create_image(0, 0, image=bg_photo, anchor='nw')

canvas.create_text(200, 30, text='Wymień walute PL', font='calibri 20 bold', fill='black')

# Ilosc
canvas.create_text(50, 95, text='Kwota:', font='calibri 19 bold', fill='black')

amount_s = IntVar()
ammount = Entry(root, textvariable=amount_s, width=13, font='calibri 16', fg='black', bd=0, bg='white')
ammount.place(x=110, y=83)

# Waluta do przeliczenia
canvas.create_text(50, 145, text='Waluta:', font='calibri 19 bold', fill='black')

currency_option = ['THB', 'GBP', 'USD', 'EUR', 'AUD', 'HUF', 'CHF', 'CZK', 'NOK', 'TRY']

option_var = StringVar()
option_var.set(currency_option[3])
currency = OptionMenu(root, option_var, *currency_option)
currency.place(x=110, y=135)

# Nowa sekcja - wynik przewalutowania
canvas.create_text(190, 190, text='Przewalutowanie', font='calibri 20 bold', fill='black')

# Button -  pokaz wynik
Button(root, text='Sprawdź kurs/kwote', font='calibri 16', fg='black', bg='white', command=act_rate).place(x=100, y=380)

# Button - pokaż dane historyczne
Button(root, text='Pokaż historie kursów', font='calibri 16', fg='black', bg='white', command=new_window_history).place(
    x=94, y=430)

# Dodatkowe info
canvas.create_text(190, 480, text='Dane z API: NBP https://api.nbp.pl/,', font='calibri 13', fill='white')

root.mainloop()
