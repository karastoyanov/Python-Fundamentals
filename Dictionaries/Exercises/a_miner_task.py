command = input()
is_running = True
count = 1
mining = {}


while is_running and command != 'stop':
    if count % 2 != 0:
        resourse = str(command)
    else:
        quantity = int(command)
        if resourse in mining:
            mining[resourse] += int(quantity)
        else:
            mining[resourse] = quantity
    count += 1
    command = input()
    if command == "stop":
        is_running = False
        break


for resourse_dict, quantity_dict in mining.items():
    print(f"{resourse_dict} -> {quantity_dict}")

