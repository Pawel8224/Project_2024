from Login_app import login_methods
import sys


login_methods.create_table(login_methods.data)

##### Front

print("Welcome! \nSign in to your system!")

while True:
    print()
    print("1. Login")
    print("2. Register account")
    print("3. Remind password")
    print("4. Exit program")
    try:
        user_choice = int(input("Choose menu: "))
    except:
        pass

    if user_choice == 1:
        login_methods.login()

    if user_choice == 2:
        login_methods.singup()

    if user_choice == 3:
        login_methods.remind_password()

    if user_choice == 4:
        print("Exit program - Bye!")
        sys.exit()

    if user_choice >= 5:
        print("There is no such number!")

login_methods.close(login_methods.data)
