user_input = input().split(", ")
numbers_list = []
list_of_results = []

for i in range(len(user_input)):
    number = int(user_input[i])
    if number % 2 == 0:
        list_of_results.append(i)
print(list_of_results)
