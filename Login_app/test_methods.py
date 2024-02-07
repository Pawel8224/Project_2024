import sqlite3
import sys

con=sqlite3.connect("Login_database.db")

def create_table(con): # tworzy tabele sqlite

    try:
        cur = con.cursor()
        cur.execute("CREATE TABLE LogPass(name, lastname, email, password, reminder)")
    except:
        pass


def login(): # loguje - zbiera dane login/haslo i sprawdza czy sa w bazie

    print("Enter your data")
    log = input("Email: ")
    pas= input("Password: ")


    cur = con.cursor()
    cur.execute("""
                SELECT password, email FROM LogPass
                """)
    result1 = cur.fetchall()
    result1_dict = dict(map(reversed,result1))




    check_login =result1_dict.get(log) # sprawdza jaka jest wartos hasla dla podanego maila

    if check_login == pas: # jezeli wartos podanego hasla zgadza się z zapisanym w bazie zwroci ok
        print("Login successful")
    else:
        print("Login failed - your password or login is incorrect!")



def singup():
    print("********************************** \n")

    print("Super that you want to create an account in our program! \nRegister your account by providing the details below:")
    sing_name= str(input("First Name: "))
    sing_lastname= str(input("Last Name: "))
    sing_email= str(input("Email: "))
    sing_password= str(input("Password: "))
    sing_remind = str(input("Give a hint to the password: "))
    sing_age = int(input("How old are you? "))
    if sing_age<18:
        print("You are too young! Leave the page")
        sys.exit()

    #################### Tabela  ########################

    cur=con.cursor()
    cur.execute("""
                INSERT INTO LogPass(name, lastname, email, password, reminder)
                VALUES(?,?,?,?,?)
                """, (sing_name,sing_lastname,sing_email,sing_password,sing_remind))
    con.commit()


def remind_password():

    cur= con.cursor()
    cur.execute("""
                SELECT email FROM LogPass
                """)
    result_remind=cur.fetchall()
    print(result_remind)
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


