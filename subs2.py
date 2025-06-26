string = input("Please type in a string: ")

start = -1

while start >= -len(string):
    print(string[start:]) #En la primera vuelta imprime t que es -1

    start -=1