password = input("Password: ")
while True:
    password2 = input("Repeat password: ")
    if password != password2:
        print("They do not match!")
    if password == password2:
        break

print("User account created! ")