number_of_heroes = int(input())
heroes = input().split(' ')
heroes_dict = {}

while True:
    number_of_heroes -= 1
    hero_name = heroes[0]
    hit_points = int(heroes[1])
    mana_points = int(heroes[2])
    heroes_dict[hero_name] = [hit_points, mana_points]
    if number_of_heroes == 0:
        break
    heroes = input().split(' ')

command = input().split(' - ')

while "End" not in command:
    if command[0] == "CastSpell":
        hero_name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        for k,v in heroes_dict.items():
            if hero_name in heroes_dict and hero_name == k:
                if mp_needed < v[1]:
                    v[1] -= mp_needed
                    print(f"{hero_name} has successfully cast {spell_name} and now has {v[0]} MP!")
                else:
                    print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command[0] == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        for k,v in heroes_dict.items():
            if hero_name in heroes_dict and hero_name == k:
                v[0] -= damage
                if v[0] > 0:
                    print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {v[0]} HP left!")
                else:
                    del heroes_dict[hero_name]
                    print(f"{hero_name} has been killed by {attacker}!")
                    break
    elif command[0] == "Recharge":
        hero_name = command[1]
        amount = int(command[2])
        for k,v in heroes_dict.items():
            if hero_name in heroes_dict and hero_name == k:
                if v[1] + amount >= 200:
                    recharged_amount = 200 - v[1]
                    v[1] = 200
                    print(f"{hero_name} recharged for {recharged_amount} MP!")
                else:
                    v[1] += amount
                    print(f"{hero_name} recharged for {amount} MP!")
    elif command[0] == "Heal":
        hero_name = command[1]
        amount = int(command[2])
        for k,v in heroes_dict.items():
            if hero_name in heroes_dict and hero_name == k:
                if v[0] + amount >= 100:
                    recharged_amount = 100 - v[0]
                    v[0] = 100
                    print(f"{hero_name} healed for {recharged_amount} HP!")
                else:
                    v[0] += amount
                    print(f"{hero_name} healed for {amount} HP!")
    command = input().split(' - ')

for k,v in heroes_dict.items():
    sorted_dict = dict(sorted(heroes_dict.items(), key = lambda x:(x[0][1], reversed == True, x[0]))) 
    print(f"{k}\n HP: {v[0]}\n MP: {v[1]}")