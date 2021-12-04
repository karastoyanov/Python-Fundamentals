user_input = input()
command = input().split(':')


while "Travel" not in command:
    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        if index < len(user_input):
            user_input = user_input[:index] + string + user_input[index:]
        print(user_input)
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < len(user_input) and end_index < len(user_input):
            user_input = user_input[:start_index] + user_input[end_index + 1:]
        print(user_input)  
    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in user_input:
            user_input = user_input.replace(old_string, new_string)
        print(user_input)
    command = input().split(':')

print(f"Ready for world tour! Planned stops: {user_input}")