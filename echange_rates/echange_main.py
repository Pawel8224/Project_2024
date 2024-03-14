
from tkinter import *
import requests



#############  DEF   #############


def act_rate():

    aft_value = float(ammount.get())
    aft_currency = option_var.get()
    body = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/')
    response = body.json()



    for rate in response[0]['rates']:
        print(rate['code'],rate['currency'],rate['mid'])
        if rate['code'] == aft_currency:
            currency_new = str(rate['code'])
            value_new = float(rate['mid'])
            sum = '%.2f' % (aft_value / float(value_new))



    Label(root, text='Waluta: ' + currency_new, font='calibri 20').place(x=100, y=250)
    Label(root, text='Kurs: ' + str(value_new),font='calibri 20').place(x=100, y=285)
    Label(root, text='Otrzymasz: ' + sum,font='calibri 20').place(x=100, y=320)





############# TKINTER  #############

root = Tk()
root.title('Przelicznik kursów walut')
root.geometry('400x500')
root.resizable(width=False, height=False)

canvas = Canvas(root, width=600, height=600)
canvas.pack(fill='both')

Label(root,text ="Przelicznik kursów walut PLN", font = 'calibri 20 bold').place(x=70,y=15)

# Ilosc
Label(root, text='Kwota:',font = 'calibri 19 bold').place(x=30,y=80)
amount_s = IntVar()
ammount = Entry(root, textvariable=amount_s, width=13, font='calibri 16',fg = 'black', bd=0,bg='white')
ammount.place(x=110, y=83)


# Waluta do przeliczenia

Label(root, text='Waluta:',font = 'calibri 19 bold').place(x=30,y=130)

currency_option = ('THB', 'GBP', 'USD','EUR','AUD','HUF','CHF','CZK','NOK','TRY')
option_var= StringVar()
currency= OptionMenu(root, option_var,*currency_option)
currency.place(x=120,y=135)

# Nowa sekcja - wynik przewalutowania
Label(root, text='Przewalutowanie', font = 'calibri 20 bold').place(x=120,y=190)


# Button -  pokaz wynik
Button(root,text= 'Sprawdź kurs/kwote', font ='calibri 16', fg='black', bg = 'white', command = act_rate).place(x=100,y=380)

root.mainloop()