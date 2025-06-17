firstnumber = int(input(("Please type in the first number: ")))

secondnumber = int(input("Please type in the second number: "))

if firstnumber > secondnumber:
    print(f"The greater number was: {firstnumber}")

elif firstnumber < secondnumber:
    print(f"The greater number was {secondnumber}")

elif firstnumber == secondnumber:
    print("The numbers are equal!")