def even_numbers(numbers):
    for i in range(len(user_input)):
        number = int(user_input[i])
        if number % 2 == 0:
            user_output.append(number)
        else:
            continue
    return user_output

user_input = input().split(" ")
user_output = []

print(even_numbers(user_output))
