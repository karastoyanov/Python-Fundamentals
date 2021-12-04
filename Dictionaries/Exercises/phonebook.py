people = input().split("-")
is_running = True
contacts = {}

while is_running:
    if len(people) > 1:
        for x in range(len(people)):
            name = people[0]
            number = people[-1]
            contacts[name] = number
            break
        people = input().split("-")
    else:
        number_to_check = int(people[0])
        is_running = False
        break
        

for v in range(number_to_check):
    name_to_check = input()
    if name_to_check in contacts:
        for a,b in contacts.items():
            print(f"{name_to_check} -> {contacts.get(name_to_check)}")
            break
    else:
        print(f"Contact {name_to_check} does not exist.")