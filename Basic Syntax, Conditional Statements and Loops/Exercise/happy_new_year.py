number = int(input())
distinct = False

while not distinct:
    number += 1
    if len(set(str(number))) == len(str(number)):
        distinct = True
print(number)
