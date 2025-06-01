print("Fill in the blank lyrics")

print("Type in the blank lyrics and see if you are as cool as me")
counter = 1 # Se pone fuera de la loop para que no se reinicie con cada iteración. No se reinicie el contador en cada intento
while True:
    lyrics = input("never wanna miss you ____")
    if lyrics == "miss" or lyrics == "miss":
      print("You got it in", counter, "attempts")

      break #Se pone para indicar cuando quiero que pare la  función, que en este caso es cuando acierta la persona.

    else:
      counter += 1
      print("Try again")

    