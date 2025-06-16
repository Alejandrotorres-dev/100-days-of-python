import math

numb_students = int(input("How many students are on the course? "))

group_size = int(input("Desired group size? "))

numb_of_groups = (f"Number of groups formed: {numb_students//group_size}")

round = math.ceil(int(numb_of_groups))

print(round)

