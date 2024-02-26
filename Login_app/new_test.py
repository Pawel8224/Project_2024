import tkinter as tk
import tkinter
from tkinter import *
from tkinter import messagebox, Entry

import sqlite3
import sys

root = Tk()
root.title('Plan Your Travel - login')
root.geometry('600x600')
root.resizable(width=False, height=False)

canvas = Canvas(root, width=600, height=600)
canvas.pack(fill = 'both',expand = True)




################### DEF ###########################
data = sqlite3.connect("file:/Users/pablom/PycharmProjects/Projekty2024/Login_app/Login_data.db", uri=True)

def create_table(data):
    try:
        cur = data.cursor()
        cur.execute("CREATE TABLE LoginPass(name, lastname, email, password, reminder,age)")
    except:
        pass

def login():

    log = EntryL.get()
    pas = EntryP.get()


    cur = data.cursor()
    cur.execute("""
                SELECT password, email FROM LoginPass
                """)
    result1 = cur.fetchall()
    result1_dict = dict(map(reversed, result1))

    check_login = result1_dict.get(log)

    if check_login == pas:
        print('OK')
        login_new_window()
    else:
        print("Login failed - your password or login is incorrect!")
        messagebox.showwarning(title='Login', message='Login failed - your password or login is incorrect!')

    #######---------MENU-------------_#############

    #while True:
    #    print("1. Show your data")
    #    print("2. Exit to menu")

    #    try:
    #        user_choice1 = int(input('Chose menu: '))
    #    except:
    #        pass

    #   if user_choice1 == 1:
    #       print("\nYour profile: \n")

        #     cur = data.cursor()
        #     cur.execute("""
        #                 SELECT name, lastname, email, password, reminder,age FROM LoginPass WHERE email = ?
        #                 """, (log,))
        #     result2 = cur.fetchall()
        #
        #     for dat in result2:
        #         result4 = dat
        #
        #     print('Name:', result4[0])
        #     print('Lastname:', result4[1])
        #     print('Email:', result4[2])
        #     print('Password:', result4[3])
        #     print('Tips Password:', result4[4])
        #     print('Age:', result4[5], '\n')
        #
        # if user_choice1 == 2:
        #     break

def login_new_window():

    window = tk.Toplevel()
    window.configure(background='grey')
    window.resizable(width=False, height=False)
    window.geometry('400x500')

    canvas2 = tk.Canvas(window, width=400, height=500)
    canvas2.pack(fill='both', expand=True)
    canvas2.pack()
    canvas2.create_text(195, 30, text='Welcome to your profile!', font='calibri 20', fill='white')




def singup():

    sing_name = str(input("First Name: "))
    sing_lastname = str(input("Last Name: "))
    sing_email = str(input("Email: "))
    sing_password = str(input("Password: "))
    sing_remind = str(input("Give a hint to the password: "))
    sing_age = int(input("How old are you? "))
    if sing_age < 18:
        print("You are too young! Leave the page")
        sys.exit()

    #################### Tabela  ########################

    cur = data.cursor()
    cur.execute("""
                INSERT INTO LoginPass(name, lastname, email, password, reminder,age)
                VALUES(?,?,?,?,?,?)
                """, (sing_name, sing_lastname, sing_email, sing_password, sing_remind, sing_age))
    data.commit()

def remind_password():
    cur = data.cursor()
    cur.execute("""
                SELECT email FROM LoginPass
                """)
    result_remind = cur.fetchall()
    e_list = list(sum(result_remind, ()))

    print("Forgot your password? No problem!")
    email_remind = str(input("Enter your email:"))

    for line in e_list:
        if line == email_remind:
            print("Your email is in the database! We have sent an email with the opportunity to reset your password.")
            break
        else:
            print("There is no such password in the database!")
            break



####################### FRONT #######################

login_ph = PhotoImage(file='/Users/pablom/Desktop/bbbb.png')
canvas.create_image(0,0,image=login_ph,anchor='nw')

#TopBar

canvas.create_text(270,80,text="Plan Your Trip! Login to platforms :)", font='calibri 20 bold', fill='white')

canvas.create_text(70, 180, text="Login", font='calibri 17 bold', fill='white')

# Login
canvas.create_text(70, 180, text="Login", font='calibri 17 bold', fill='white')

frameL  = Frame(root,width=200, height=20, bg='white').place(x=130,y=170)
EntryL = Entry(frameL,width=19, font='calibri 17', bd=0, bg='#e4eaf5', fg='black')
EntryL.place(x=130,y=167)
login_button = Button(root,text='Login', font= 'calibri 17', fg = 'black', bg = 'white', command=login).place(x=195,y=270)



# Password
canvas.create_text(70, 243, text="Password", font='calibri 17 bold', fill='white')

frameP = Frame(root, width=200, height=20, bg='white').place(x=130,y=230)
EntryP = Entry(frameP, width=19, font='calibri 17', bd=0, bg='#e4eaf5', fg='black')
EntryP.place(x=130,y=230)

# Remind Passwords

remind_pass = Button(root, text='Forgot Your Password?', font='calibri 16', fg='black', bd=0, bg='white',command= remind_password).place(x=130, y=320)

# Register Accounts

canvas.create_text(230,400, text='You dont have accounts? Sing up!',font='calibri 17 bold', fill='white')
singup_button = Button(root, text='Sing Up', font='calibri 17', fg='black', bd=0, bg='white',command= singup).place(x=180,y=420)



root.mainloop()
