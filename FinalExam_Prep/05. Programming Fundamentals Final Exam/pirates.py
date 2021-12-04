cities = input().split('||')
cities_dict = {}

while "Sail" not in cities:
    city = cities[0]
    population = int(cities[1])
    gold = int(cities[2])
    if city not in cities_dict:
        cities_dict[city] = [population, gold]
    else:
        for k,v in cities_dict.items():
            if city == k:
                v[0] += population
                v[1] += gold
                break
    cities = input().split('||')
    
command = input().split('=>')

while "End" not in command:
    if command[0] == "Plunder":
        town = command[1]
        people = int(command[2])
        gold = int(command[3])
        if town in cities_dict:
            for k,v in cities_dict.items():
                if k == town:
                    v[0] -= people
                    v[1] -= gold
                    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
                    if v[0] <= 0 or v[1] <= 0:
                        del cities_dict[town]
                        print(f"{town} has been wiped off the map!")
                    break
    elif command[0] == "Prosper":
        town = command[1]
        gold = int(command[2])
        for k,v in cities_dict.items():
            if k == town:
                if gold >  0:
                    v[1] += gold
                    print(f"{gold} gold added to the city treasury. {town} now has {v[1]} gold.")
                else:
                    print("Gold added cannot be a negative number!")
    command = input().split("=>")            
                
if len(cities_dict) > 0:        
    print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
    for k,v in sorted(cities_dict.items(), key = lambda x: (-x[1][1], x[0])):
         print(f"{k} -> Population: {v[0]} citizens, Gold: {v[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed")