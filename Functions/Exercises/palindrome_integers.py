def palindrome_check(check_number):
    for i in range(len(user_input)):
        number = user_input[i]
        if number == number[::-1]:
            print("True")
        else:
            print("False")
    return user_output


user_input = input().split(", ")
user_output = ''

print(palindrome_check(user_output))
