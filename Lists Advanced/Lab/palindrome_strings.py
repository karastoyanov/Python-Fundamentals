user_input = input().split(" ")
palindrome_check = input()
result_list = []
count = 0

for x in range(len(user_input)):
    to_check = str(user_input[x])
    if to_check == to_check[::-1]:
        result_list.append(to_check)    


print(result_list)
print(f"Found palindrome {result_list.count(palindrome_check)} times")
