first_word = input(("Please type in the first word: "))

second_word = input(("Please type in the second word: "))

if second_word > first_word:
    print(f"{second_word} comes alphabetically last")

elif second_word < first_word:
    print(f"{first_word} comes alphabetically last")



elif second_word == first_word:
    print("You gave the same word twice")