def sorted_numbers(final_list):
    for index in range(len(user_input)):
        number = int(user_input[index])
        user_output.append(number)
    return sorted(user_output, reverse=False)

user_input = input().split(" ")
user_output = []
result = sorted_numbers(user_output)

print(result)
