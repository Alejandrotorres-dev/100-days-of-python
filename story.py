story = ""
previous= ""

while True:
    words = input("Please type in a word: ")
    
    if words == "end" or words == previous:
        break  # Sale del bucle si se repite la palabra

    story += words + " "  # Agrega un espacio para separar las palabras
    previous = words  # Actualiza la palabra anterior

print(story)

1. Al principio:
python
Copiar
Editar
story = ""
previous = ""
La historia está vacía. No hay palabra anterior.

2. Primera vuelta del bucle:
🔹 El usuario escribe: hola

Se evalúa:

words == "end" → ❌

words == previous → hola == "" → ❌

Entonces:

Se ejecuta: story += "hola " → story = "hola "

Se actualiza: previous = "hola"

✅ Continúa el bucle

3. Segunda vuelta:
🔹 El usuario escribe: mundo

Se evalúa:

words == "end" → ❌

words == previous → mundo == hola → ❌

Entonces:

Se agrega: story = "hola mundo "

Se actualiza: previous = "mundo"

✅ Continúa el bucle

4. Tercera vuelta:
🔹 El usuario escribe: mundo (la misma palabra)

Se evalúa:

words == "end" → ❌

words == previous → mundo == mundo → ✅

💥 Se ejecuta break, y el bucle se detiene aquí