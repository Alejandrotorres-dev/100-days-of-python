word = input("Word: ")

frame = 30

espacio = 30 - 2 - len(word)

left_spaces = espacio // 2  
right_spaces = espacio - left_spaces

firstline = "*" * frame
middleline = "*" + " " * left_spaces + word + " " * right_spaces + "*"
lastline = "*" * frame

print(firstline)
print(middleline)
print(lastline)
