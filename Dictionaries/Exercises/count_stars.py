user_input = input()
my_dict = {}

for letter in user_input:
    if letter == " ":
        pass
    else:
        if letter not in my_dict:
            my_dict[letter] = 1
        else:
            my_dict[letter] += 1

keys_list = list(my_dict.keys())
values_list = list(my_dict.values())

for i in range(len(keys_list)):
    key = keys_list[i]
    for v in range(len(values_list)):
       value = values_list[i]
    print(f'{key} -> {value}')