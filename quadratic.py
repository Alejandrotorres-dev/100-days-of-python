from math import sqrt

value_a = int(input("Introduce the value of a: "))

value_b = int(input("Introduce the value of b: "))

value_c = int(input("Introduce the value of c: "))

equation1 = (-value_b + sqrt(value_b**2 - 4*value_a*value_c)) / (2 * value_a)
equation2 = (-value_b - sqrt(value_b**2 - 4*value_a*value_c)) / (2 * value_a)

print((f"{equation1} and {equation2}"))




