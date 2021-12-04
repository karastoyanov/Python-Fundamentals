n = int(input())
sum1 = 0
for index in range(1, n):
    if n % index == 0:
        sum1 = sum1 + index

if sum1 == n:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
