def odd_numbers(sum_odd):
    for i in range(len(number)):
        check_number = int(number[i])
        if check_number % 2 != 0:
            odd_list.append(check_number)
        else:
            continue
    return sum_odd


def even_numbers(sum_even):
    for i in range(len(number)):
        check_number = int(number[i])
        if check_number % 2 == 0:
            even_list.append(check_number)
        else:
            continue
    return sum_even


number = input()
odd_list = []
even_list = []
result_odd = odd_numbers(odd_list)
result_even = even_numbers(even_list)


print(f"Odd sum = {sum(result_odd)}, Even sum = {sum(result_even)}")
