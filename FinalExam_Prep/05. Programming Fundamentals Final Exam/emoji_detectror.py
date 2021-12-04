import re
# import numpy as np


user_input = input()
pattern = r"::[A-Z][a-z]{2,}::|\*+[A-Z][a-z]{2,}\*+"
matches = re.findall(pattern, user_input)
numbers = re.findall("\d", user_input)

total_threshold = 1
for i in numbers:
    total_threshold *= int(i)
    
print(f"Cool threshold: {total_threshold}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")

total_ascii_value = 0

for _ in range(len(matches)):
    current_match = str(matches[_])
    for i in range(len(current_match)):
        char = current_match[i]
        if char.isalpha():
            pass
        else:
            current_match = current_match.replace(char, '')
            break
    for x in range(len(current_match)):
        char = current_match[x]
        ascii_value = ord(char)
        total_ascii_value += ascii_value
    if total_ascii_value > total_threshold:
        print(f"{matches[_]}")
    total_ascii_value = 0    
