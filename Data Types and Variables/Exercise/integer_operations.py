import math

num_one = int(input())
num_two = int(input())
num_three = int(input())
num_four = int(input())

result = (num_one + num_two)
result = math.floor(result / num_three)
result = result * num_four
print(f"{result:.0f}")
