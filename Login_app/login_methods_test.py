from __future__ import print_function
import sqlite3
import sys
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

data = sqlite3.connect("file:/Users/pablom/PycharmProjects/Projekty2024/Login_app/Login_data.db", uri=True)


def create_table(data):
    try:
        cur = data.cursor()
        cur.execute("CREATE TABLE LoginPass(name, lastname, email, password, reminder,age)")
    except:
        pass


def login():
    print("Enter your data")
    log = input(str("Email: "))
    pas = input("Password: ")

    cur = data.cursor()
    cur.execute("""
                SELECT password, email FROM LoginPass
                """)
    result1 = cur.fetchall()
    result1_dict = dict(map(reversed, result1))

    check_login = result1_dict.get(log)

    if check_login == pas:
        print("Login successful")
    else:
        print("Login failed - your password or login is incorrect!")

    #######---------MENU-------------_#############

    while True:
        print("1. Show your data")
        print("2. Exit to menu")

        try:
            user_choice1 = int(input('Chose menu: '))
        except:
            pass

        if user_choice1 == 1:
            print("\nYour profile: \n")

            cur = data.cursor()
            cur.execute("""
                        SELECT name, lastname, email, password, reminder,age FROM LoginPass WHERE email = ?
                        """, (log,))
            result2 = cur.fetchall()

            for dat in result2:
                result4 = dat

            print('Name:', result4[0])
            print('Lastname:', result4[1])
            print('Email:', result4[2])
            print('Password:', result4[3])
            print('Tips Password:', result4[4])
            print('Age:', result4[5], '\n')

        if user_choice1 == 2:
            break


def singup():
    print("********************************** \n")

    print(
        "Super that you want to create an account in our program! \nRegister your account by providing the details below:")
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
    global email_remind
    email_remind = str(input("Enter your email:"))


    for line in e_list:
        if line == email_remind:
            print("Your email is in the database! We have sent an email with the opportunity to reset your password.")
            client_send_email()
            break
        else:
            print("There is no such password in the database!")
            break

def client_send_email():


    message = Mail(
        from_email='pawel.milewski01@gmail.com',
        to_emails=email_remind,
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))

