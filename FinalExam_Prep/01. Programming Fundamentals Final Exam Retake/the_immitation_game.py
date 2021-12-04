message = input()


while True:
    command = input().split("|")
    if "Move" in command:
        number_of_letters = int(command[-1])
        first_part = message[number_of_letters:]
        second_part = message[:number_of_letters]
        message = first_part + second_part
    if "Insert" in command:
        index = int(command[-2])
        value = command[-1]
        first_part = message[:index]
        second_part = message[index:]
        message = first_part + value + second_part        
    if "ChangeAll" in command:
        substring = command[-2]
        replacement = command[-1]
        message = message.replace(substring, replacement)
    if "Decode" in command:
        break
    
print(f"The decrypted message is: {message}")
