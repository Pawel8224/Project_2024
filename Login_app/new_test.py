import tkinter
from tkinter import *

root = Tk()
root.title('Plan Your Travel - login')
root.geometry('600x600')
root.resizable(width=False, height=False)

canvas = Canvas(root, width=600, height=600)
canvas.pack(fill = 'both',expand = True)




#### DEF









#### FRONT

login_ph = PhotoImage(file='/Users/pablom/Desktop/bbbb.png')
canvas.create_image(0,0,image=login_ph,anchor='nw')

canvas.create_text(text='Login')







root.mainloop()
