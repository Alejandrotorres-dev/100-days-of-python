#if = Do some code only IF some condition is True

#     Else do something else, es como lo ultimo a lo que se acude.
# Antes podemos utilizar elif, elseif

age = int(input("Enter your age: "))
if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You havent been born yet!") 
else:
    print("You must be 18+ to sign up")


#if age >= 18:
    #print("You are now signed up!")
#elif age < 0:
    #print("You havent been born yet!") 
#elif age >= 100:
    #print("You are too old to sign up")
#else:
    #print("You must be 18+ to sign up")

# Si escribo -1 se salta la primera condicion que es falsa la de if. Y tiene lugar la elif ya que es verdadera, y salta el else statement.

# De esta Manera si pongo 101 Pondra you are signed up porque primero pasa por if age >= 18
# Por ello vamos a cambiar el orden como vemos arriba, lo ponemos como if el primero y lo que antes estaba arriba 
#Pasa a segundo lugar como elif