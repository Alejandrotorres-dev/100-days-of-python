print ("Exam Grade Calculator")

name = input("Whats the name of the exam ")

print ("Max. Possible Score:", 100)

score = int(input("Your Score: "))
if score <= 40 and score <= 50:
    print("You got", score, "%" " wich is a U")

elif score >50 and score <=60 :
    print("You got", score, "%" " wich is a D")

elif score >60 and score <= 70 :
    print("You got", score, "%" " wich is a C")

elif score >70 and score <= 80 :
    print("You got", score, "%" " wich is a B")

elif score >80 and score <= 90 :
    print("You got", score, "%" " wich is a A-")

elif score >90 :
    print("You got", score, "%" " wich is a A+")