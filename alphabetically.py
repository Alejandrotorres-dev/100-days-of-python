letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

# Compara combinaciones posibles para encontrar la del medio
if (letter1 < letter2 < letter3) or (letter3 < letter2 < letter1):
    middle = letter2
elif (letter2 < letter1 < letter3) or (letter3 < letter1 < letter2):
    middle = letter1
else:
    middle = letter3

print("The letter in the middle is " + middle)