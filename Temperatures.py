temperature_f = int(input("Please type in a temperature (F): "))
 
temperature_c = (temperature_f - 32) * 5/9
 
print(f"{temperature_f} degrees Fahrenheit equals {temperature_c} degrees Celsius")
 
if temperature_c < 0:
    print("Brr! It's cold in here!")
 