import re
text = input()
user_list = []


pattern = r'!([A-Za-z]+)!:\[([A-Za-z]+)\]'
matches = re.finditer(pattern, text)
if matches.group() is not None:
    for match in matches:
        command = match.group(2)
        message = match.group(4)
        
    for _ in range (len(message)):
        char = ord(message[_])
        user_list.append(str(char))
        
    print(f"{command}: ")
    print(" ".join(user_list))
else:
    print("The message is not valid")