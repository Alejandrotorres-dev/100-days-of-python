import random

def rollDice(sides):
  result = random.randint(1,sides)
  return result

def roll_6_and_8():
  roll_6 = rollDice(6)
  roll_8 = rollDice(8)
  health = roll_6 * roll_8
  return health
print("⚔️Character stats generator⚔️")
  
haveACharacter = "yes"
while haveACharacter == "yes":
  character = input("Name your warrior: ")
  health = (roll_6_and_8())
  print("Their health is ", health,"hp" ) 
  haveACharacter = input("Want to create another character?")



