import re

nm_inputs = int(input())
user_list = []

while nm_inputs > 0:
    password = input()
    pattern = r"([\$][A-Z][a-z]{2,}[$]|[%][A-Z][a-z]{2,}[%]): .([0-9]{1,}).\|.([0-9]{1,}).\|.([0-9]{1,}).\|"
    matches = re.finditer(pattern, password)
    if matches:
        for match in matches:
            first_number = int(match.group(2))
            second_number = int(match.group(3))
            third_number = int(match.group(4))
    else:
        print("Valid message not found!")
    nm_inputs -= 1