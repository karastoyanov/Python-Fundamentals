number = int(input())
word = input()
list_strings = []
list_contents = []

for i in range(number):
    contents = input()
    list_contents.append(contents)
    if word in contents:
        list_strings.append(contents)

print(list_contents)
print(list_strings)
