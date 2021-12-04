coffee_counter = 0
is_running = True
lower_cases = ("dog", "cat", "coding", "movie")
upper_cases = ("DOG", "CAT", "CODING", "MOVIE")


while is_running is True:
    user_input = input()
    if user_input in lower_cases:
        coffee_counter += 1
    elif user_input in upper_cases:
        coffee_counter += 2
    elif user_input == "END":
        is_running = False
        break
    else:
        continue

if coffee_counter <= 5:
    print(coffee_counter)
else:
    print("You need extra sleep")
