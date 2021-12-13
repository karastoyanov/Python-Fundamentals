skill = input()
command = input().split(" ")

while True:
    if "GladiatorStance" in command:
        skill = skill.upper()
        print(skill)
    elif "DefensiveStance" in command:
        skill = skill.lower()
        print(skill)
    elif "Dispel" in command:
        index = int(command[1])
        letter = command[2]
        if index < len(skill):
            skill = skill.replace(skill[index], letter, 1)
            print("Success!")
        else:
            print("Dispel too weak.")
    elif command[1] == "Change":
        first_substring = command[2]
        second_substring = command[3]
        if first_substring in skill:
            skill = skill.replace(first_substring, second_substring)
            print(skill)
    elif command[1] == "Remove":
        substring = command[2]
        if substring in skill:
          skill = skill.replace(substring, "")
          print(skill) 
    elif command[1] == "Azeroth":
        break
    else:
        print("Command doesn't exist!")
        
    
    command = input().split(" ")