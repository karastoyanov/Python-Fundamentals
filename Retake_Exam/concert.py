import re

command = input()
concert_bands = {}
total_time = 0
new_dict = {}

while "Start!" not in command:
    if "Add" in command:
        command = re.split("; |, ", command)
        if command[1] not in concert_bands:
            concert_bands[command[1]] = [command[2::], [0]]
        else:
            for _ in range(len(command[2::])):
                member = command[2::][_]
                for k,v in concert_bands.items():
                    if k == command[1]:
                        if member in v[0]:
                            pass
                        else:
                            v[0].append(member)
                            break
        
    elif "Play" in command:
        command = command.split("; ")
        band_name = command[1]
        time = int(command[2])
        total_time += time
        if band_name in concert_bands:
            for k, v in concert_bands.items():
                if band_name in concert_bands:
                    if band_name == k:
                    # play_time = int(v[1]) + time
                        concert_bands[band_name] = [v[0], [v[1][0] + time]]
                        break
        else:
            concert_bands[band_name] = [[],[time]]
            
    
    command = input()
    
print(f"Total time: {total_time}")
# for k, v in sorted(concert_bands.items()):
#     print(f"{k} -> {v[1][0]}")
#     new_dict[k] = v[1][0]

for k, v in sorted(concert_bands.items()):
    print(f"{k} -> ")
    print(sorted({v[1][0]}, reverse = True))
    new_dict[k] = v[1][0]
    
all_values = new_dict.values()
max_value = max(all_values)
for k,v in sorted(concert_bands.items()):
    if v[1][0] == max_value:
        # print(f"{k}\n=> ")
        names = '\n=> '.join(v[0])
        print(f"{k}\n=> " + f"{names}")