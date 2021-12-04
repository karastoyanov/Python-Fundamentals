activation_key = input()
command = input().split(">>>")

while "Generate" not in command:
    if "Contains" in command:
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif "Flip" in command:
        start_index = int(command[2])
        end_index = int(command[3])
        if command[1] == "Upper":
            substring = activation_key[start_index:end_index]
            activation_key = activation_key[:start_index] + substring.upper() + activation_key[end_index:]
            print(activation_key)
        else:
            substring = activation_key[start_index:end_index]
            activation_key = activation_key[:start_index] + substring.lower() + activation_key[end_index:]
            print(activation_key)
    elif "Slice" in command:
        start_index = int(command[1])
        end_index = int(command[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]    
        print(activation_key)
    command = input().split(">>>")

print(f"Your activation key is: {activation_key}")