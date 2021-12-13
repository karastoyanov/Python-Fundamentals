import re

user_number = int(input())
counter = 0

while user_number > 0:
    data = input()
    pattern = r'(U\$)([A-Z][a-z]{2,})(U\$)(P\@\$)([A-z]{5,}[0-9]{1,})(P\@\$)' # Groups 2 and 5
    matches = re.finditer(pattern, data)
    if re.search(pattern, data) is None:
        print("Invalid username or password")
    
    for match in matches:
        if match:
            print("Registration was successful")
            counter += 1
            user_name = match.group(2)
            password = match.group(5)
            print(f"Username: {user_name}, Password: {password}")
            break
    user_number -= 1

print(f"Successful registrations: {counter}")