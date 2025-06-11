import random  

print("Infinity Dice 🎲")  

usersides = int(input("How many sides?: "))  




def rollDice(sides):
    print("You rolled ", random.randint(1, sides))  


while playGame == "yes":
    rollDice(usersides)  
    playGame = input("Roll again?") 
