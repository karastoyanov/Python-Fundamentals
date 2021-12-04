start = int(input())
end = int(input())
all_symbols = ' '

for character in range(start, end + 1):
    all_symbols += chr(character) + " "
print(all_symbols)