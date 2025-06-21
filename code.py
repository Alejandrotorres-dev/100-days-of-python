attempts = 1

while True:
    pin = int(input("PIN: "))
    if pin != 4321:
        attempts += 1
        print("Wrong")
    elif pin == 4321 and attempts ==1:
        print("Correct! It only took you one single attempt!")
        break
    elif pin == 4321:
        print(f" Correct! It took you {attempts} attempts")
        break


