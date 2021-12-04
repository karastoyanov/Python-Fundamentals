energy = int(input())
command = input()
won_battles = 0
fights = 0


while command != "End of battle":
    distance = int(command)
    if energy < distance:
        break
    if energy >= distance:
        energy -= distance
        won_battles += 1
        if won_battles % 3 == 0 and won_battles != 0:
            energy += won_battles
    fights += 1
    command = input()
    

if energy >= distance:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")