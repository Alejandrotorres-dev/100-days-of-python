print("Welcome to The Game One-Million-To-One")

print("Guest a number between 1 to 1.000.000, if the number is to low i will say low if its high i will say high")
correctnumber = 2300
attempts = 1

while True:
    answer = int(input("Guess the number: "))
    if attempts < 0:
        print ("We will never know")
        exit()
    elif answer < correctnumber:
        print("It is to low")
        attempts += 1
    
    elif answer > correctnumber:
        print("It is to High")
        attempts +=1
    
    elif answer == correctnumber:
        print("Correct")
        break
    else:
        print("That is not a number that I recognize")

print("It tooks you",attempts,"to get it Correct." ) #Esto va fuera para que se imprima tras el break.