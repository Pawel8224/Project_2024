from tkinter import *
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

currency_option = ['THB', 'GBP', 'USD', 'EUR', 'AUD', 'HUF', 'CHF', 'CZK', 'NOK','TRY']

option_var = StringVar()
option_var.set(currency_option[3])
currency = OptionMenu(root, option_var, *currency_option)
currency.place(x=110, y=135)

# Nowa sekcja - wynik przewalutowania
canvas.create_text(190, 190, text='Przewalutowanie', font='calibri 20 bold', fill='black')

# Button -  pokaz wynik
Button(root, text='Sprawdź kurs/kwote', font='calibri 16', fg='black', bg='white', command=act_rate).place(x=100, y=380)

# Wyświetlanie wyniku
# lbl_curr = Label(root, text = '', font='calibri 20').place(x=140, y=250)
# lbl_value = Label(root, text = '', font='calibri 20').place(x=140, y=280)
# lbl_sum = Label(root, text = '', font='calibri 20').place(x=140, y=300)


root.mainloop()
