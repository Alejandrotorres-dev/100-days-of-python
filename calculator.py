number1 = int(input("Give me a number: "))

number2 = int(input("Give me a second number"))

operation = input("What operation? ")

if operation == "add":
    print(f"{number1} + {number2} = {number1 + number2}")

if operation == "multiply":
    print(f"{number1} * {number2} = {number1 * number2}")

if operation == "subtract":
    print(f"{number1} - {number2} = {number1 - number2}")

else:
    exit

print(operation)

