pieces_number = int(input())
pieces_dict = {}

while pieces_number > 0:
    pieces_with_composer = input().split("|")
    pieces_number -= 1
    for _ in pieces_with_composer:
        piece = pieces_with_composer[0]
        composer = pieces_with_composer[1]
        key = pieces_with_composer[2]
        pieces_dict[piece] = [composer, key]
        break
    if pieces_number == 0:
        break


while True:
    command = input().split("|")
    if "Add" in command:
        piece = command[1]; composer = command[2]; key = command[3]
        if piece not in pieces_dict:
            add_dict = {}
            add_dict[piece] = [composer, key]
            pieces_dict.update(add_dict)
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    if "Remove" in command:
        piece = command[1]
        if piece in pieces_dict:
            del pieces_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    if "ChangeKey" in command:
        piece = command[1]
        new_key = command[2]
        if piece in pieces_dict:
            pieces_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection!")
    if "Stop" in command:
        break
    

for key, value in sorted(pieces_dict.items()):
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")