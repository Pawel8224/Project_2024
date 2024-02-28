import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title('Plan Your Travel - login')
root.geometry('600x600')
root.resizable(width=False, height=False)

canvas = Canvas(root, width=600, height=600)
canvas.pack(fill='both', expand=True)

################### DEF ###########################

data = sqlite3.connect("file:/Users/pablom/PycharmProjects/Projekty2024/Login_app/Login_data.db", uri=True)


def create_table(data):
    try:
        cur = data.cursor()
        cur.execute("CREATE TABLE LoginPass(name, lastname, email, password, reminder,age)")
    except:
        pass


def login():
    global log
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


def login_new_window():
    window = tk.Toplevel()
    window.configure(background='grey')
    window.resizable(width=False, height=False)
    window.geometry('400x500')

    canvas2 = tk.Canvas(window, width=400, height=500)
    canvas2.pack(fill='both', expand=True)

    canvas2.create_text(195, 30, text='Welcome to your profile!', font='calibri 20', fill='white')

    cur = data.cursor()
    cur.execute("""
                     SELECT name, lastname, email, password, reminder,age FROM LoginPass WHERE email = ?
                 """, (log,))
    result2 = cur.fetchall()

    for dat in result2:
        result4 = dat
    Label(window, text="First name: " + result4[0]).place(x=20, y=70)
    Label(window, text="Last name: " + result4[1]).place(x=20, y=95)
    Label(window, text="Email: " + result4[2]).place(x=20, y=120)
    Label(window, text="Password: " + result4[3]).place(x=20, y=145)
    Label(window, text="Hint: " + result4[4]).place(x=20, y=170)
    Label(window, text="Age: " + str(result4[5])).place(x=20, y=195)


def singup_tabel():
    sn = sing_name.get()
    sl = sing_lastname.get()
    se = sing_email.get()
    sp = sing_password.get()
    sr = sing_remind.get()
    sa = sing_age.get()

    cur = data.cursor()
    cur.execute("""
                    INSERT INTO LoginPass(name, lastname, email, password, reminder,age)
                    VALUES(?,?,?,?,?,?)
                    """, (sn, sl, se, sp, sr, sa))
    data.commit()
    messagebox.showinfo(title='Register', message='Great! Your account has been created!')


def singup_window():
    window_singup = tk.Toplevel(root)
    window_singup.grab_set()
    window_singup.title("Sing up")
    window_singup.resizable(width=False, height=False)
    window_singup.geometry('400x500')


    Label(window_singup,
          text="Greate that you want to create an account in our program! \nRegister your account by providing the details below:",
          font='calibri 12 bold').place(x=19, y=10)

    global sing_name
    global sing_lastname
    global sing_email
    global sing_password
    global sing_remind
    global sing_age

    # frame_name = Frame(window_singup, width=70, height=18, bg='grey').place(x=150,y=70)

    Label(window_singup, text="First name: ", font='calibri 16 bold').place(x=40, y=69)
    sing_n = StringVar()
    sing_name = Entry(window_singup, textvariable=sing_n, width=18, font='calibri 17', bd=0, bg='white', fg='black')
    sing_name.place(x=150, y=70)


    Label(window_singup, text="Last name: ", font='calibri 16 bold').place(x=40, y=118)
    sing_l = StringVar()
    sing_lastname = Entry(window_singup, textvariable=sing_l, width=18, font='calibri 17', bd=0, bg='#e4eaf5',fg='black')
    sing_lastname.place(x=150, y=120)

    Label(window_singup, text="Email: ", font='calibri 16 bold').place(x=40, y=169)
    sing_e = StringVar()
    sing_email = Entry(window_singup, textvariable=sing_e, width=18, font='calibri 17', bd=0, bg='#e4eaf5', fg='black')
    sing_email.place(x=150, y=170)

    Label(window_singup, text="Password: ", font='calibri 16 bold').place(x=40, y=220)
    sing_p = StringVar()
    sing_password = Entry(window_singup, textvariable=sing_p, width=18, font='calibri 17', bd=0, bg='#e4eaf5',fg='black')
    sing_password.place(x=150, y=220)

    Label(window_singup, text="Hint: ", font='calibri 16 bold').place(x=40, y=268)
    sing_r = StringVar()
    sing_remind = Entry(window_singup, textvariable=sing_r, width=18, font='calibri 17', bd=0, bg='#e4eaf5', fg='black')
    sing_remind.place(x=150, y=270)

    Label(window_singup, text="Age: ", font='calibri 16 bold').place(x=40, y=315)
    sing_a = StringVar()
    sing_age = Entry(window_singup, textvariable=sing_a, width=18, font='calibri 17', bd=0, bg='#e4eaf5', fg='black')
    sing_age.place(x=150, y=320)

    Button(window_singup, text='Sing up', font='calibri 16', fg='black', bd=0, bg='white', command=singup_tabel).place(x=190, y=380)



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
create_table(data)

login_ph = PhotoImage(file='/Users/pablom/PycharmProjects/Projekty2024/Login_app/bbbb.png')
canvas.create_image(0, 0, image=login_ph, anchor='nw')

# TopBar

canvas.create_text(270, 80, text="Plan Your Trip! Login to platforms :)", font='calibri 20 bold', fill='white')
canvas.create_text(70, 180, text="Login", font='calibri 17 bold', fill='white')

# Login
canvas.create_text(70, 180, text="Login", font='calibri 17 bold', fill='white')
EntryL = Entry(root, width=19, font='calibri 17', bd=0, bg='#e4eaf5', fg='black')
EntryL.place(x=130, y=167)

Button(root, text='Login', font='calibri 17', fg='black', bg='white', command=login).place(x=195, y=270)

# Password
canvas.create_text(70, 243, text="Password", font='calibri 17 bold', fill='white')
EntryP = Entry(root, width=19, font='calibri 17', bd=0, bg='#e4eaf5', fg='black', show='*')
EntryP.place(x=130, y=230)


# Remind Passwords

Button(root, text='Forgot Your Password?', font='calibri 16', fg='black', bd=0, bg='white',command=remind_password).place(x=130, y=320)

# Register Accounts

canvas.create_text(230, 400, text='You dont have accounts? Sing up!', font='calibri 17 bold', fill='white')
Button(root, text='Sing Up', font='calibri 17', fg='black', bd=0, bg='white', command=singup_window).place(
    x=180, y=420)



root.mainloop()

