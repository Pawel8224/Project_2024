from customtkinter import *
import customtkinter
from PIL import Image
import PIL
from tkinter import Canvas
import os


app = CTk()
canvas1=CTkCanvas(app,width=490, height=830)

#BackImage = CTkImage(light_image=Image.open("/Users/pablom/PycharmProjects/Pliki/distance_app/newbg.png"),size=(490, 830))
#image_label=CTkLabel(app,image = BackImage,text='').place(x=0,y=0)


BackImage = CTkImage(light_image=Image.open("/Users/pablom/PycharmProjects/Pliki/distance_app/newbg.png"),size=(490, 830))
image_label=CTkLabel(master=app,image = BackImage,text='').place(x=0,y=0)
image_label.grid(row=0, column=0, pady=(0, 20))

app.geometry("490x830")
app.title("Plan Your Trip")
app.resizable(width=False, height=False)


#set_appearance_mode("system")


# ---------------------------METHODS ------------------------ #

# BACKGROUNG






# --------------------------- FRONTEND ------------------------ #



# BACKGROUND

#BackImage = CTkImage(light_image=Image.open("/Users/pablom/PycharmProjects/Pliki/distance_app/newbg.png"),size=(490, 830))

#image_label=CTkLabel(app,image = BackImage,text='').place(x=0,y=0)




# OKNO - START PODROZY ------------------------


addres0=StringVar
addres_entry0= CTkEntry(app,width=190,font=('Calibri',20))
addres_entry0.place(x=180,y=150)

labelO = CTkLabel(master=app,text='ORIGIN', font=('Calibri',22))
labelO.place(x=60,y=152)


# OKNO - KONIEC PODROZY ------------------------

addresD=StringVar
addres_entryD = CTkEntry(master=app,width=190,font=('Calibri',20))
addres_entryD.place(x=180,y=220)

labelD=CTkLabel(master=app,text='DESTINATION', font=('Calibri',20),)
labelD.place(x=32,y=222)


# OKNO - SPALANIE ------------------------

gas_entry = CTkEntry(master=app,width=190,font=('Calibri',20))
gas_entry.place(x=180,y=285)

labelGas = CTkLabel(master=app,text='Fuel Usage',font=('Calibri',22))
labelGas.place(x=32,y=260)


# OKNO - CENA PALIWA ------------------------






# CHECKBOX - ODCINKI PLATNE ------------------------






# CHECKBOX - AUTOSTRADY   ------------------------








# BUTTON - POKAZ WYNIK/WYCZYSC

img = Image.open("/Users/pablom/PycharmProjects/Projekty2024/TravelApp/Icon/a.png")

summary_button = CTkButton(master=app, text = 'SUMMARY', font=('Arial', 15),corner_radius=35, fg_color='#ba882b',hover_color='#4158D0',border_width=0,
                           image=CTkImage(dark_image=img,light_image=img))
summary_button.place(x=145,y=480)




















app.mainloop()
