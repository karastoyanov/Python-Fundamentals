countries = list(x for x in input().split(', '))
capitals = list(v for v in input().split(', '))
user_dictionary = {}


for i in range(len(countries)):
    country_arg = countries[i]
    for v in range(len(capitals)):
        capital_arg = capitals[i]
        user_dictionary[country_arg] = capital_arg
        break

for x,y in user_dictionary.items():
    print(f"{x} -> {y}")