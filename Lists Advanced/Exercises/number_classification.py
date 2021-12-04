user_input = [int(s) for s in input().split(", ")]
positive_numbers = []
negative_numbers = []
even_numbers = []
odd_numbers = []


for number in range(len(user_input)):
    current_number = int(user_input[number])
    if current_number >= 0:
        positive_numbers.append(current_number)
    if current_number < 0:
        negative_numbers.append(current_number)
    if current_number % 2 == 0:
        even_numbers.append(current_number)
    if current_number % 2 != 0:
        odd_numbers.append(current_number)

print(f"Positive: {', '.join(str(s) for s in positive_numbers)}")
print(f"Negative: {', '.join(str(s) for s in negative_numbers)}")
print(f"Even: {', '.join(str(s) for s in even_numbers)}")
print(f"Odd: {', '.join(str(s) for s in odd_numbers)}")

