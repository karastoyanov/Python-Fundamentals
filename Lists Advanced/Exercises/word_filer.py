user_input = [word for word in input().split(" ")]
user_output = []

for index in range(len(user_input)):
    current_word = str(user_input[index])
    if len(current_word) % 2 == 0:
        print(current_word)
        
