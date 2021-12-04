number = int(input())

for x in range(number):
    for y in range(number):
        for z in range(number):
            print(f'{chr(97+ x)}{chr(97 + y)}{chr(97 + z)}')
