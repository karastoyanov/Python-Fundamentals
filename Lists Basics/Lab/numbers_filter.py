number_input = int(input())
list_of_numbers = []
filtered = []

for i in range(number_input):
    number = int(input())
    list_of_numbers.append(number)

command = input()

if command == 'even':
    for number in list_of_numbers:
        if number % 2 == 0:
            filtered.append(number)
elif command == 'odd':
    for number in list_of_numbers:
        if number % 2 != 0:
            filtered.append(number)
elif command == "negative":
    for number in list_of_numbers:
        if number < 0:
            filtered.append(number)
elif command == "positive":
    for number in list_of_numbers:
        if number >= 0:
            filtered.append(number)

print(filtered)
