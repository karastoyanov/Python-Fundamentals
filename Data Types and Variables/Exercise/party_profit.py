import math

group_size = int(input())
days = int(input())
days_count = 0
coins = 0
coins_for_food = 2
coins_for_water = 3
coins_for_mot_party = 2


for _ in range(days):
    days_count += 1
    coins += 50
    coins -= coins_for_food
    if days_count % 10 == 0:
        group_size -= 2
    elif days_count % 15 == 0:
        group_size += 5
    elif days_count % 3 == 0:
        coins -= coins_for_water
    elif days_count % 5 == 0:
        coins += 20
        coins -= coins_for_mot_party

total_coins = math.floor(coins) / group_size
print(f"{group_size} companions received {math.floor(total_coins)} coins each.")
