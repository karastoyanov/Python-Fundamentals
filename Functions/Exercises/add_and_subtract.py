def sum_numbers(first, second):
    return first + second


def substrach(sum, third):
    return sum - third


a = int(input())
b = int(input())
c = int(input())
sum_of_f_two_digits = sum_numbers(a, b)
result = substrach(sum_of_f_two_digits, c)

print(result)
