def get_symbols(first, second):
    collected_symbols = []
    for current_symbol in range(ord(first) + 1, ord(second)):
        collected_symbols.append(chr(current_symbol))
    return collected_symbols
    
    
string_one = input()
string_two = input()
result = get_symbols(string_one, string_two)

print(' '.join(result))
