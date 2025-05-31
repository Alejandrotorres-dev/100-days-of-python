#Typecasting = the process of converting a variable from one data type to another 
#              str(), int(), float(), bool()
#This is useful when we want to manage user input. Wich is always a string. Y en algunas ocasiones querremos convertirla a int, float o bool
name = "Alejandro" #Alejandro es una string, una serie de caracteres.
age = 25
gpa = 3.2
is_student = True

#convert or gpa to an integer, ahora es un float ya que es 3.2

gpa = int(gpa)

print(gpa) #this prints a 3, que es un integer

#age = str(age)

#print(age) #Convertimos la edad que es un integer a una string,cadena de texto.

#name = bool(name)

#print(name)