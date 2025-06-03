# Imprimo el mensaje de bienvenida al juego
print("Welcome to Math Facts Game")
print("How well do you know your math facts? Pick a number and I will give you 10 math facts to solve.")

# El usuario introduce un número para practicar sus multiplicaciones
fact_family = int(input("Name your multiples: "))  # Convierto la entrada del usuario a un número entero


# Contador para contar las respuestas correctas
counter = 0

# Bucle para mostrar 10 preguntas de multiplicación
for i in range(1, 11):  # Desde el 1 hasta el 10
  correct_answer = i * fact_family  # Calcula la respuesta correcta de la multiplicación
  print(i, "x", fact_family)  # Muestro al usuario lo que tiene que resolver
  
  answer = int(input("> "))  # Pide al usuario que introduzca su respuesta

  if answer == correct_answer:
    # Si la respuesta es correcta, muestra un mensaje y aumenta el contador
    print("You got it right!")
    counter += 1
  else:
    # Si no es correcta, muestra la respuesta correcta
    print("That's not correct. It should have been", correct_answer)

# Después del bucle, verifico cuántas respuestas correctas tuvo el usuario
if counter == 10:
  print("Wow! A perfect score! 🥳")  # Mensaje especial si respondió todo bien
else:
  print("You got", counter, "out of 10 correct.")  # Muestra el total de respuestas correctas








