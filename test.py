numbers = [int(x) for x in input().split(' ')]
text = input()
message_list = []

for _ in range (len(numbers)):
    current_number = numbers[_]
    current_list = [int(x) for x in str(current_number)]
    current_number = sum(current_list)
    for i in range(len(text)):
        if current_number < len(text):
            character = text[current_number]
            message_list.append(character)
            text = text.replace(text[current_number], "", 1)
            break
        else:
            difference = current_number - len(text)
            character = text[difference]
            message_list.append(character)
            text = text.replace(text[current_number - len(text)], "", 1)
            break
        
print("".join(message_list))