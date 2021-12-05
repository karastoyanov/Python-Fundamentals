password = input()
command = input().split(' ')

while "Complete" not in command:
    if "Upper" in command:
        index = int(command[2])
        old_char = password[index]
        password = password.replace(old_char, old_char.upper())
        print(password)
    if "Lower" in command:
        index = int(command[2])
        old_char = password[index]
        password = password.replace(old_char, old_char.lower())
    if "Insert" in command:
        index = int(command[1])
        char = command[2]
        first_part = password[:index]
        second_part = password[index:]
        password = first_part + char + second_part
        print(password)
    if "Replace" in command:
        char = command[1]
        if char in password:
            value = int(command[2])   
            ascii_value = ord(char) + value
            new_symbol = chr(ascii_value)
            password = password.replace(char, new_symbol)
            print(password)
    if "Validation" in command:
        char = "_"
        if len(password) < 8:
            print("PAssword must be at least 8 characters long!")
        if char not in password and password.isalnum() is False:
            print("Password must consist only of leters, digits and _!")
        if password.islower():
            print("Password must consist at least one uppercase letter!")
        if password.isupper():
            print("Password must consist at least one lowercase letter!")
        if password.isalpha():
            print("Password must consist at least one digit!")
        
    command = input().split(' ')