def increment(n1, n2, n3):
    if first > second and first > third:
        return first
    elif second > first and second > third:
        return second
    else:
        return third

first = int(input())
second = int(input())
third = int(input())

print(increment(first, second, third))


