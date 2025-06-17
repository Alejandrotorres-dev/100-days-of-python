name1= input("Write a name: ")

age1 = int(input("Write an age: "))

name2 = input("Write another name: ")

age2 = int(input("Write another age: "))

if age2 < age1:
    print(f"The elder one is {name1}")

elif age2 > age1:
    print(f"The elder one is {name2}")

elif age2 == age1:
    print(f"{name1}and{name2} are the same age")
