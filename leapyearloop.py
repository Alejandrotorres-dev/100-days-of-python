start_year = int(input("Year: "))
year = start_year + 1 #Empieza a buscar desde al año siguiente si pussite 2023 entonces year sera 2024
#Si el bucle comenzara con 2024 y entra al loop y ve que si es leap year el output seria El next year despues de 2024 es 2024
#y eso no tiene sentido.

while True:
    if year % 100 == 0:
        if year % 400 == 0:
            break
    elif year % 4 == 0:
        break

    year += 1 #Sino hemos encontrado un año bisiesto pues busca el siguiente.

print(f"The next leap year after {start_year} is {year}")