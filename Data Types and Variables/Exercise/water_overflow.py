capacity = 255
nm_of_pours = int(input())
litters_in_pool = 0

for i in range(nm_of_pours):
    litters = int(input())
    litters_in_pool += litters
    if litters_in_pool <= capacity:
        nm_of_pours -= 1
    else:
        print("Insufficient capacity!")
        litters_in_pool -= litters
        nm_of_pours -= 1
        continue
if nm_of_pours == 0:
    print(litters_in_pool)
