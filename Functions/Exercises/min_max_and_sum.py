def solve_func(min_number):
    for index in range(len(user_input)):
        number = int(user_input[index])
        user_output.append(number)
    return user_output


user_input = input().split(" ")
user_output = []
min_result = min(solve_func(user_output))
max_result = max(solve_func(user_output))
sum_result = sum(solve_func(user_output))

print(f"The minimum number is {min_result}")
print(f"The maximum number is {max_result}")
print(f"The sum number is: {sum_result // 3}")
