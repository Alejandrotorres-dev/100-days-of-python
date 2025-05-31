cuenta = float(input("Cuanto os habeis gastado? "))

porcentaje = int(input("cuanto quereis dejar de propina? "))

grupo = int(input("Cuantos sois? "))

propina = porcentaje / 100 * cuenta

totalconpropina = propina + cuenta

porpersona = totalconpropina / 3

print(round(porpersona, 2))