user_input = (input())
user_list = user_input.split(', ')
scanner = -1
for i in user_list:
    if user_list[-1] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    else:
        scanner -= 1
        if user_list[scanner] == "wolf":
            warned_sheep = scanner + 1
            print(f"Oi! Sheep number {abs(warned_sheep)}! You are about to be eaten by a wolf!")
            break
