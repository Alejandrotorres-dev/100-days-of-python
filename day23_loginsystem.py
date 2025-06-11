print("Login system")

correct_username = "alejandro"
correct_password = "buenas"

def login():
    while True:
        username = input("What is your username?: ")
        password = input("What is your password?: ")
        if username == correct_username and password == correct_password:
            print("Welcome to replit!")
            break
        else:
            print("Incorrect, try again")
            

login()
