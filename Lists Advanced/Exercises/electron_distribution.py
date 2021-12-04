number_of_electrons = int(input())
shields_list = []
shells_list = []
difference = 0


for index in range(1, number_of_electrons + 1):
    shields = 2*(index * index)
    shields_list.append(shields)
    if sum(shields_list) <= number_of_electrons:
        shells_list.append(shields)
        if sum(shields_list) + shields > number_of_electrons:
            difference = number_of_electrons - sum(shields_list)
            if sum(shields_list) < number_of_electrons:
                shells_list.append(difference)


print(shells_list)