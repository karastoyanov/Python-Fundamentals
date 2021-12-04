text_message = input()
text_message.replace(" ","")

for char in range(len(text_message)):
    symbol = text_message[char]
    next_symbol = ord(symbol) + 3
    print(chr(next_symbol), end = '')