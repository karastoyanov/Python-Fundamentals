key = int(input())
nm_lines = int(input())
character = ''
output = []

for _ in range(nm_lines):
    character = input()
    output.append(chr(ord(character) + key))

print(''.join(output))
