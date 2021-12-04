password = input()
command = input().split(' ')


while "Done" not in command:
    if command[0] == "TakeOdd":
        new_password = []
        for i in range(len(password)):
            char = password[i]
            if i % 2 != 0:
                new_password.append(char)
        password = "".join(new_password)
        print(password) 
    elif command[0] == "Cut":
        index = int(command[1])
        lenght = int(command[2])
        substring = password[index:index + lenght]
        password = password.replace(substring, "", 1)
        print(password)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    command = input().split(' ')
    
    
print(f"Your password is: {password}")