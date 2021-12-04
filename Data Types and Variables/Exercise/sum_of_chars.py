# sourcery skip: for-index-underscore
characters = int(input())
sum_of_ascii_values = 0

for char in range(characters):
    next_character = input()
    sum_of_ascii_values += ord(next_character)
print(f"The sum equals: {sum_of_ascii_values}")
