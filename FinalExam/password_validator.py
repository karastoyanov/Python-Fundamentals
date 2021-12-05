password = input()
command = input().split(" ")

while command[0] != "Complete":
    if "Upper" in command:
        index = int(command[2])
        old_char = password[index]
        new_char = password[index].upper()
        password = password.replace(old_char, new_char, 1)
        print(password)
    elif "Lower" in command:
        index = int(command[2])
        old_char = password[index]
        new_char = password[index].lower()
        password = password.replace(old_char, new_char, 1)
        print(password)
    elif "Insert" in command:
        index = int(command[1])
        char = command[2]
        if index < len(password):
            first_part = password[:index]
            second_part = password[index:]
            password = first_part + char + second_part
            print(password)
    elif "Replace" in command:
        char = command[1]
        value = int(command[2])
        if char in password:
            ascii_value = ord(char)
            new_value = ascii_value + value
            new_symbol = chr(new_value)
            password = password.replace(char, new_symbol)
            print(password)
    elif "Validation" in command:
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        if not password.isalnum():
            print("Password must consist only of letters, digits and _!")
        if password.find("_") != -1:
            print("Password must consist only of letters, digits and _!")
        if password.islower():
            print("Password must consist at least one uppercase letter!")
        if password.isupper():
            print("Password must consist at least one lowercase letter!")
        if password.isalpha():
            print("Password must consist at least one digit!")   
    command = input().split(" ")