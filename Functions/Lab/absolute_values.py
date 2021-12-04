user_input = input().split(" ")
user_output = []

for i in user_input:
    number = abs(float(i))
    user_output.append(number)
    
print(user_output)
