message = input()
command = input().split(' ')

while True:
    if command[0] == "Replace":
        current_char = command[1]
        new_char = command[2]
        message = message.replace(current_char, new_char)
        print(message)
    elif command[0] == "Cut":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index <= len(message) and end_index <= len(message):
            substring = message[start_index:end_index + 1]
            message = message.replace(substring, "")
            print(message)
        else:
            print("Invalid indexes!")
    elif command[0] == "Make":
        args = command[1]
        if args == "Upper":
            message = message.upper()
        elif args == "Lower":
            message = message.lower()
        print(message)
    elif command[0] == "Check":
        string = command[1]
        if string in message:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")
    elif command[0] == "Sum":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(message) and 0 <= end_index < len(message):
            sum_ind = 0
            substring = message[start_index:end_index + 1]
            for char in substring:
                sum_ind += ord(char)
            print(sum_ind)
        else:
            print("Invalid indexes!")
    elif command[0] == "Finish":
        break
    command = input().split(' ')