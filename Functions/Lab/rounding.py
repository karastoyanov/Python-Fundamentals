user_input = input().split()
user_output = []

for i in range(len(user_input)):
    number = float(user_input[i])
    user_output.append(round(number))

print(user_output)
