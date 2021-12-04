count = int(input())
parking = {}

for _ in range(count):
    data = input()
    split_data = data.split(" ")
    command = split_data[0]
    
    
    if command == "register":
        user_name = split_data[1]
        license = split_data[2]
        if user_name in parking:
            print(f"ERROR: already registered with plate number {license}")
        else:
            parking[user_name] = license
            print(f"{user_name} registered {license} successfully")
        
    elif command == "unregister":
        user_name = split_data[1]
        if user_name not in parking:
            print(f"ERROR: user {user_name} not found")
        else:
            del parking[user_name]
            # parking.pop(user_name)
            print(f"{user_name} unregistered successfully")

for user_name, license in parking.items():
    print(f"{user_name} => {license}")
    