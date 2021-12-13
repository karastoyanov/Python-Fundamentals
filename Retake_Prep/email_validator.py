user_mail = input()
command = input().split(" ")
ascii_list = []

while "Complete" not in command:
    if "Upper" in command:
        for _ in range(len(user_mail)):
            letter = user_mail[_]
            if letter.isalpha():
                user_mail = user_mail.replace(letter, letter.upper())
        print(user_mail)
    elif "Lower" in command:
        for _ in range(len(user_mail)):
            letter = user_mail[_]
            if letter.isalpha():
                user_mail = user_mail.replace(letter, letter.lower())
        print(user_mail)
    elif "GetDomain" in command:
        count = -int(command[1])
        print(user_mail[count::])
    elif "GetUsername" in command:
        if "@" in user_mail:
            substring = []
            for _ in range(len(user_mail)):
                symbol = user_mail[_]
                if symbol != "@":
                    substring.append(symbol)
                else:
                    break
            print("".join(substring))
        else:
            print(f"The email {user_mail} doesn't contain the @ symbol.")
    elif "Replace" in command:
        char = command[1]
        user_mail = user_mail.replace(char, "-")
        print(user_mail)
    elif "Encrypt" in command:
        for _ in range(len(user_mail)):
            symbol = user_mail[_]
            ascii_value = str(ord(symbol))
            ascii_list.append(ascii_value)
        print(" ".join(ascii_list))
        ascii_list = []
    command = input().split(" ")