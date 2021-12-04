first_list = input().split(", ")
second_list = input().split(', ')
match = []

for word in first_list:
    for words in second_list:
        if word in words and not word in match:
            match.append(word)
print(match)
    