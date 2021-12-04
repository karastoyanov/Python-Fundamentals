message = input()

while True:
    command = input().split(":|:")
    args = command[0]
    if args == "InsertSpace":
        index = int(command[-1])
        first_part = message[:index] + " " 
        second_part = message[index:]
        message = first_part + second_part
        print(message)
    if args == "Reverse":
        substring = command[-1]
        if substring in message:
                message = message.replace(substring, substring[::-1], 1)
                print(message)               
        else:
            print("error")         
    if args == "ChangeAll":
        substring = command[-2]
        replacement = command[-1]
        if substring in message:
            message = message.replace(substring, replacement)
            print(message)
    if "Reveal" in command:
        break
    
print(f"You have a new text message: {message}")