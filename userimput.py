#input() = A function that prompts the user to enter data
#          Return the entered data as a sting

name = input("What is your name: ") #la promp es lo que ponemos entre comillas para que el usuario sepa lo que le estamos preguntando. 
#Name es una variable. Cuando aceptamos la input del usuario nos devuelve la info como una string data type

age = int(input("How old are you?: ")) #esta la typecasteamos a otro type en este caso int porque lo necesitamos para age

#age = int(age) #hacemos esto para convertir la edad a una integer y que lo reconozca como numero y le sume mas 1. en la linea 7 
#se hace de forma mas condensada con el mismo resultado

age = age + 1

print(f"Hello {name}!") #Usamos la f string si queremos insertar variables, en este caso es name.
print("Happy birthday!") 
print(f"You are {age} years old")