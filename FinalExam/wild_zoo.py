command = input().split(": ")
animals = {}

while "EndDay" not in command:
    if command[0] == "Add":
        args = command[1].split("-")
        animal_name = args[0]
        needed_food = int(args[1])
        area = args[2]
        animals[area] = [animal_name, needed_food]
    elif command[0] == "Feed":
        args = command[1].split("-")
        animal_name = args[0]
        food = int(args[1])
        if animal_name in animals:
            for k,v in animals.items():
                v[1] -= food
                if v[1] <= 0:
                    del animals[animal_name]
                    print(f"{animal_name} was successfully fed")
    command = input().split(":")