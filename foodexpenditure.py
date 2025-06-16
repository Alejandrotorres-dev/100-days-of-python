times_a_week = int(input("How many times a week do you eat at the student cafeteria? "))

price_of_luch = float(input("Whats the price of a typical student lunch? "))

money_groceries_weekly = float(input("How much money do you spend on groceries in a week"))
total = (times_a_week * price_of_luch) + money_groceries_weekly
print(f"Daily: {total / 7} ")
print(f"Weekly: {total} euros")