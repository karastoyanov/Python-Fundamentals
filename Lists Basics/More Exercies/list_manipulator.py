user_list = [int(x) for x in input().split(' ')]
command = input().split(' ')

while "end" not in command:
    if command[0] == "exchange":
        index = int(command[1])
        if index > len(user_list) or index < 0:
            print("Invalid index")
        else:
            user_list = user_list[index + 1:] + user_list[:index + 1]
    elif command[0] == "max":
        if command[1] == "even":
            even_numbers = []
            for _ in range(len(user_list)):
                number = user_list[_]
                if number % 2 == 0:
                    even_numbers.append(number)
                if len(even_numbers) == 0:
                    print("No matches")
                else:
                    print(even_numbers.index(max(even_numbers)))
        elif command[1] == "odd":
            odd_numbers = []
            for _ in range(len(user_list)):
                number = user_list[_]
                if number % 2 != 0:
                    odd_numbers.append(number)
            if len(odd_numbers) == 0:
                print("No matches")
            else:
                print(odd_numbers.index(max(odd_numbers)))
    elif command[0] == "min":
        if command[1] == "even":
            even_numbers = []
            for _ in range(len(user_list)):
                number = user_list[_]
                if number % 2 == 0:
                    even_numbers.append(number)
            if len(even_numbers) == 0:
                print("No matches")
            else:
                print(even_numbers.index(min(even_numbers)))
        elif command[1] == "odd":
            odd_numbers = []
            for _ in range(len(user_list)):
                number = user_list[_]
                if number % 2 == 0:
                    odd_numbers.append(number)
            if len(odd_numbers) == 0:
                print("No matches")
            else:
                print(odd_numbers.index(min(odd_numbers)))
    elif command[0] == "first":
        count = int(command[1])
        if command[2] == "even":
            even_numbers = []
            for _ in range(len(user_list), count):
                number = user_list[_]
                if number % 2 == 0:
                    even_numbers.append(number)
            print(even_numbers)        
        elif command[2] == "odd":
            odd_numbers = []
            for _ in range(len(user_list), count):
                number = user_list[_]
                if number % 2 != 0:
                    odd_numbers.append(number)
            print(odd_numbers)
    elif command[0] == "last":
        count = int(command[1])
        reversed_list = reversed(user_list)
        if command[2] == "even":
            even_numbers = []
            for _ in range(len(reversed_list), count):
                number = reversed_list[_]
                if number % 2 == 0:
                    even_numbers.append(number)
            print(even_numbers)
        elif command[2] == "odd":
            odd_numbers = []
            for _ in range(len(reversed_list), count):
                number = reversed_list[_]
                if number % 2 != 0:
                    odd_numbers.append(number)
            print(odd_numbers)
    
    command = input().split(' ')