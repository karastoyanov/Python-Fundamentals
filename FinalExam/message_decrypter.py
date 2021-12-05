import re

nm_inputs = int(input())
user_list = []

while nm_inputs > 0:
    message = input()
    pattern = r"([\$][A-Z][a-z]{2,}[$]|[%][A-Z][a-z]{2,}[%]): .([0-9]{1,}).\|.([0-9]{1,}).\|.([0-9]{1,}).\|"
    matches = re.finditer(pattern, message)
    if matches:
        for match in matches:
            if match.group(2) and match.group(3) and match.group(4):
                first_number = int(match.group(2))
                second_number = int(match.group(3))
                third_number = int(match.group(4))
                first_char = chr(first_number)
                second_char = chr(second_number)
                third_char = chr(third_number)
                print(first_char + second_char + third_char)
            elif len(matches) > 30:
                print("Valid message not found!")
    else:
        print("Valid message not found!")
    
    nm_inputs -= 1